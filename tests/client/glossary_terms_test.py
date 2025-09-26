"""
Tests for the GlossaryTerms endpoint.
"""

import lokalise
import pytest
from lokalise.client import Client

PROJECT_ID = "6504960967ab53d45e0ed7.15877499"
GLOSSARY_TERM_ID = 5319746


@pytest.mark.vcr
def test_glossary_terms(client: Client) -> None:
    """Tests glossary terms fetching with cursor"""
    glossary_terms = client.glossary_terms(PROJECT_ID, {"limit": 2})

    glossary_term = glossary_terms.items[0]

    assert glossary_term.term == "router"

    assert glossary_terms.next_cursor == "5489103"
    assert glossary_terms.has_next_cursor()
    assert not glossary_terms.has_next_page()


@pytest.mark.vcr
def test_glossary_term(client: Client) -> None:
    """Tests single glossary term fetching"""
    glossary_term = client.glossary_term(PROJECT_ID, GLOSSARY_TERM_ID)

    assert glossary_term.term == "router"
    assert glossary_term.projectId == PROJECT_ID
    assert glossary_term.description == "A network device"
    assert not glossary_term.caseSensitive
    assert glossary_term.translatable
    assert not glossary_term.forbidden
    assert glossary_term.translations[0]["langId"] == 597
    assert glossary_term.tags == []
    assert glossary_term.createdAt == "2025-03-31 15:01:00 (Etc/UTC)"
    assert glossary_term.updatedAt is None


@pytest.mark.vcr
def test_create_glossary_terms(client: Client) -> None:
    """Tests creation of glossary terms"""

    glossary_terms = client.create_glossary_terms(
        PROJECT_ID,
        [
            {
                "term": "python",
                "description": "sample desc",
                "caseSensitive": False,
                "forbidden": False,
                "translatable": True,
                "tags": ["term1"],
            },
            {
                "term": "code editor",
                "description": "",
                "caseSensitive": False,
                "forbidden": False,
                "translatable": True,
                "translations": [
                    {
                        "langId": 674,
                        "translation": "éditeur de code",
                        "description": (
                            "Logiciel permettant d’écrire, modifier "
                            "et organiser du code informatique."
                        ),
                    }
                ],
                "tags": ["term2"],
            },
        ],
    )

    assert len(glossary_terms.items) == 2

    term0 = glossary_terms.items[0]
    term1 = glossary_terms.items[1]

    assert term0.term == "python"
    assert term1.tags == ["term2"]


@pytest.mark.vcr
def test_create_glossary_terms_error(client: Client) -> None:
    """Tests creation of glossary terms with error"""

    with pytest.raises(lokalise.errors.ClientError) as excinfo:
        client.create_glossary_terms(
            PROJECT_ID,
            [
                {
                    "term": "python",
                    "description": "sample desc",
                    "caseSensitive": False,
                    "forbidden": False,
                    "translatable": False,
                }
            ],
        )

    assert excinfo.value.args[1] == 422


@pytest.mark.vcr
def test_update_glossary_terms(client: Client) -> None:
    """Tests updating of glossary terms"""
    new_term_desc = "A commonly used network device"

    glossary_terms = client.update_glossary_terms(
        PROJECT_ID, [{"id": GLOSSARY_TERM_ID, "description": new_term_desc, "caseSensitive": False}]
    )

    glossary_term = glossary_terms.items[0]

    assert glossary_term.description == new_term_desc
    assert glossary_term.id == GLOSSARY_TERM_ID


@pytest.mark.vcr
def test_delete_glossary_terms(client: Client) -> None:
    """Tests deletion of glossary terms"""

    response = client.delete_glossary_terms(PROJECT_ID, [5489361, 5489360])

    deleted_info = response["data"]["deleted"]

    assert deleted_info["count"] == 2
    assert 5489360 in deleted_info["ids"]
