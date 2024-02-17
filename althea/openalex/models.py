"""althea/openalex/models.py"""

from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, HttpUrl, validator

# fmt: off
WorkID = str

AuthorID = str
AuthorPosition = str

InstitutionID = str
OrcidID = str
RorID = str
RorType = str

ApcProvenance = str

OALocationVersion = str

DOI = str
PMID = str
PMCID = str

WwwUrl = str
WebUrl = Union[HttpUrl, WwwUrl]


# fmt: on


class InvertedIndex(BaseModel):
    """Inverted index of the abstract of a paper"""

    terms: Optional[dict[str, list[int]] | list[int]] = None


class Author(BaseModel):
    """Author of a paper"""

    id: Optional[AuthorID] = None
    display_name: Optional[str] = None
    orcid: Optional[OrcidID] = None


class Institution(BaseModel):
    """Institution of an author of a paper"""

    id: Optional[InstitutionID] = None
    display_name: Optional[str] = None
    ror: Optional[RorID] = None
    country_code: Optional[str] = None
    type: Optional[RorType] = None


class Authorship(BaseModel):
    """Authorship of a paper"""

    author_position: Optional[AuthorPosition] = None
    author: Optional[Author] = None
    institutions: Optional[list[Institution]] = None


class APC(BaseModel):
    """Article Processing Charge of a paper"""

    value: Optional[int] = None
    currency: Optional[str] = None
    provenance: Optional[ApcProvenance] = None
    value_usd: Optional[int] = None


class Biblio(BaseModel):
    """Old-timey bibliographic info for this work"""

    volume: Optional[str] = None
    issue: Optional[str] = None
    first_page: Optional[str] = None
    last_page: Optional[str] = None


class Concept(BaseModel):
    """Concept of a paper"""

    id: Optional[HttpUrl] = None
    wikidata: Optional[HttpUrl] = None
    display_name: Optional[str] = None
    level: Optional[int] = None
    score: Optional[float] = None


class ExternalIDs(BaseModel):
    """
    All the external identifiers that we know about for this work.
    IDs are expressed as URIs whenever possible.
    """

    doi: Optional[DOI] = None
    mag: Optional[int] = None
    openalex: Optional[WorkID] = None
    pmid: Optional[PMID] = None
    pmcid: Optional[PMCID] = None


class OALocation(BaseModel):
    """Open Access location of a paper"""

    is_oa: Optional[bool] = None
    landing_page_url: Optional[WebUrl] = None
    pdf_url: Optional[WebUrl] = None
    source: Optional[dict[str, bool | str | list[str] | None]] = None
    license: Optional[str] = None
    version: Optional[OALocationVersion] = None


class YearCount(BaseModel):
    """Year count of a paper"""

    year: Optional[int] = None
    cited_by_count: Optional[int] = None


class Ngram(BaseModel):
    """Ngram of a paper""" ""

    ngram: Optional[str] = None
    ngram_count: Optional[int] = None
    ngram_tokens: Optional[int] = None
    term_frequency: Optional[float] = None


class OpenAccess(BaseModel):
    """Open Access information of a paper""" ""

    is_oa: Optional[bool] = None
    oa_status: Optional[str] = None
    oa_url: Optional[HttpUrl] = None
    any_repository_has_fulltext: Optional[bool] = None


class MeshTag(BaseModel):
    """MeSH tag of a paper"""

    descriptor_ui: Optional[str] = None
    descriptor_name: Optional[str] = None
    qualifier_ui: Optional[str] = None
    qualifier_name: Optional[str] = None
    is_major_topic: Optional[bool] = None


class SDG(BaseModel):
    """Sustainable Development Goal of a paper"""

    id: Optional[HttpUrl] = None
    display_name: Optional[str] = None
    score: Optional[float] = None


class Grant(BaseModel):
    """Grant of a paper"""

    funder: Optional[HttpUrl] = None
    funder_display_name: Optional[str] = None
    award_id: Optional[str] = None


class WorkObject(BaseModel):
    """Work object of a paper"""

    abstract_inverted_index: Optional[InvertedIndex] = None
    authorships: Optional[list[Authorship]] = None
    apc_list: Optional[APC] = None
    apc_paid: Optional[APC] = None
    best_oa_location: Optional[OALocation] = None
    biblio: Optional[Biblio] = None
    cited_by_api_url: Optional[HttpUrl] = None
    cited_by_count: Optional[int] = None
    concepts: Optional[list[Concept]] = None
    corresponding_author_ids: Optional[list[HttpUrl]] = None
    corresponding_institution_ids: Optional[list[HttpUrl]] = None
    countries_distinct_count: Optional[int] = None
    counts_by_year: Optional[list[YearCount]] = None
    created_date: Optional[date] = None
    display_name: Optional[str] = None
    doi: Optional[HttpUrl] = None
    fulltext_origin: Optional[str] = None
    grants: Optional[list[Grant]] = None
    has_fulltext: Optional[bool] = None
    id: Optional[HttpUrl] = None
    ids: Optional[ExternalIDs] = None
    institutions_distinct_count: Optional[int] = None
    is_paratext: Optional[bool] = None
    is_retracted: Optional[bool] = None
    language: Optional[str] = None
    license: Optional[str] = None
    locations: Optional[list[OALocation]] = None
    locations_count: Optional[int] = None
    mesh: Optional[list[MeshTag]] = None
    ngrams_url: Optional[HttpUrl] = None
    open_access: Optional[OpenAccess] = None
    primary_location: Optional[OALocation] = None
    publication_date: Optional[date] = None
    publication_year: Optional[int] = None
    referenced_works: Optional[list[HttpUrl]] = None
    related_works: Optional[list[HttpUrl]] = None
    sustainable_development_goals: Optional[list[SDG]] = None
    title: Optional[str] = None
    type: Optional[str] = None
    type_crossref: Optional[str] = None
    updated_date: Optional[datetime] = None


class WorkNGram(BaseModel):
    """Ngram object of a paper"""

    ngram: Optional[str] = None
    ngram_count: Optional[int] = None
    ngram_tokens: Optional[int] = None
    term_frequency: Optional[float] = None


class WorkOpenAccess(BaseModel):
    """Open Access object of a paper"""

    any_repository_has_fulltext: Optional[bool] = None
    is_oa: Optional[bool] = None
    oa_status: Optional[str] = None
    oa_url: Optional[HttpUrl] = None

    @validator("oa_url", pre=True, always=True)
    def validate_oa_url(cls, v, values, config, field):  # noqa
        if v is None:
            return v
        try:
            return HttpUrl(v, scheme="https")
        except ValueError:
            return None
