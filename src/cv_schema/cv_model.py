from pydantic import BaseModel, Field, ConfigDict

from cv_schema.education import Education
from cv_schema.experience import Experience
from cv_schema.teaching import Teaching
from cv_schema.personal import Personal
from cv_schema.google_scholar_author import GoogleScholarAuthor
from cv_schema.publication import Publication
from cv_schema.affiliation import Affiliation
from cv_schema.institution import Institution
from cv_schema.coauthor import CoAuthor
from cv_schema.research import Research
from cv_schema.security import Security
from cv_schema.social import Social
from cv_schema.grant import Grant
from cv_schema.news import News


class CVModel(BaseModel):

    title: str

    news: list[News] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    experiences: list[Experience] = Field(default_factory=list)
    teaching: list[Teaching] = Field(default_factory=list)
    publications: list[Publication] = Field(default_factory=list)
    coauthors: list[CoAuthor] = Field(default_factory=list)
    grants: list[Grant] = Field(default_factory=list)
    affiliations: list[Affiliation] = Field(default_factory=list)
    institutions: list[Institution] = Field(default_factory=list)

    personal: Personal
    social: Social
    research: Research
    google_scholar_author: GoogleScholarAuthor
    security: Security

    long_intro: str
    short_intro: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
