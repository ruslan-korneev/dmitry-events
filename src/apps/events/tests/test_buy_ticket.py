import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_profile(api_client):
    client = api_client()
    response = client.post(
        reverse("event-buy-ticket", kwargs={"pk": 1}),
        data={"owner": "+71231234567"},
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
