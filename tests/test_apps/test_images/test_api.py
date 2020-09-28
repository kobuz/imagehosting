import io

import pytest
from PIL import Image
from rest_framework.test import APIClient

from server.apps.users.models import User


@pytest.fixture()
def api_user():
    return User.objects.create()


@pytest.fixture()
def api_client(api_user):
    client = APIClient()
    client.force_authenticate(api_user)
    return client


@pytest.fixture()
def upload_image():
    file = io.BytesIO()
    image = Image.new("RGBA", size=(300, 300), color=(155, 0, 0))
    image.save(file, "png")
    file.name = "test.png"
    file.seek(0)
    return file


@pytest.mark.django_db
def test_upload_image(api_client, api_user, upload_image):
    response = api_client.put(
        "/images/upload/",
        data={"file": upload_image},
        format="multipart",
    )
    assert response.status_code == 204
    assert api_user.image_set.count() == 1
