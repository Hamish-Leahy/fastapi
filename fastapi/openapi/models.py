from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Type, Union

from fastapi._compat import (
    PYDANTIC_V2,
    CoreSchema,
    GetJsonSchemaHandler,
    JsonSchemaValue,
    _model_rebuild,
    with_info_plain_validator_function,
)
from fastapi.logger import logger
from pydantic import AnyUrl, BaseModel, Field
from typing_extensions import Annotated, Literal, TypedDict
from typing_extensions import deprecated as typing_deprecated

try:
    import email_validator

    assert email_validator  # make autoflake ignore the unused import
    from pydantic import EmailStr
except ImportError:  # pragma: no cover

    class EmailStr(str):  # type: ignore
        @classmethod
        def __get_validators__(cls) -> Iterable[Callable[..., Any]]:
            yield cls.validate

        @classmethod
        def validate(cls, v: Any) -> str:
            logger.warning(
                "email-validator not installed, email fields will be treated as str.\n"
                "To install, run: pip install email-validator"
            )
            return str(v)

        @classmethod
        def _validate(cls, __input_value: Any, _: Any) -> str:
            logger.warning(
                "email-validator not installed, email fields will be treated as str.\n"
                "To install, run: pip install email-validator"
            )
            return str(__input_value)

        @classmethod
        def __get_pydantic_json_schema__(
            cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
        ) -> JsonSchemaValue:
            return {"type": "string", "format": "email"}

        @classmethod
        def __get_pydantic_core_schema__(
            cls, source: Type[Any], handler: Callable[[Any], CoreSchema]
        ) -> CoreSchema:
            return with_info_plain_validator_function(cls._validate)


class Contact(BaseModel):
    name: Optional[str] = None
    url: Optional[AnyUrl] = None
    email: Optional[EmailStr] = None

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class License(BaseModel):
    name: str
    identifier: Optional[str] = None
    url: Optional[AnyUrl] = None

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class Info(BaseModel):
    title: str
    summary: Optional[str] = None
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class ServerVariable(BaseModel):
    enum: Annotated[Optional[List[str], Field(min_length=1)] = None
    default: str
    description: Optional[str] = None

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class Server(BaseModel):
    url: Union[AnyUrl, str]
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class Reference(BaseModel):
    ref: str = Field(alias="$ref")


class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]] = None


class XML(BaseModel):
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class ExternalDocumentation(BaseModel):
    description: Optional[str] = None
    url: AnyUrl

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}
    else:

        class Config:
            extra = "allow"


class Schema(BaseModel:
    # ... (remaining code)
