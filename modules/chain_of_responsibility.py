from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractStringProcess(ABC):

    @abstractmethod
    def set_next_string_process(self, string_process: AbstractStringProcess) -> AbstractStringProcess:
        pass

    @abstractmethod
    def process(self, text: str) -> str:
        pass


class StringProcessBase(AbstractStringProcess):
    __next_string_process: AbstractStringProcess

    def set_next_string_process(self, string_process: AbstractStringProcess) -> AbstractStringProcess:
        self.__next_string_process = string_process
        return string_process

    @abstractmethod
    def process(self, text) -> str:
        print("StringProcessBase")
        try:
            return self.__next_string_process.process(text)
        except AttributeError:
            return text


class StringProcessLowerCase(StringProcessBase):
    def process(self, text) -> str:
        print("StringProcessLowerCase")
        if text.isupper():
            return super().process(text.lower())
        else:
            raise InterruptedError("Erro durante processo de lower case.")


class StringProcessRemoveUnderscore(StringProcessBase):
    def process(self, text) -> str:
        print("StringProcessRemoveUnderscore")
        if "_" in text:
            return super().process(text.replace("_", ""))
        else:
            raise InterruptedError("Erro durante remoção do underscore.")


class StringProcessChangeToTitle(StringProcessBase):
    def process(self, text) -> str:
        print("StringProcessChangeToTitle")
        if not text.istitle():
            return super().process(text.title())
        else:
            raise InterruptedError("Erro durante mudança para titulo")


class StringProcessDefault(StringProcessBase):
    def process(self, text) -> str:
        print("StringProcessDefault")
        if text:
            return text
        else:
            return None


if __name__ == "__main__":
    sp_change_to_title = StringProcessChangeToTitle()
    sp_remove_underscore = StringProcessRemoveUnderscore()
    sp_lower_case = StringProcessLowerCase()

    sp_lower_case \
        .set_next_string_process(sp_remove_underscore) \
        .set_next_string_process(sp_change_to_title)

    print(f"Resultado : {sp_lower_case.process('ASDASD__ASDDS')}")
