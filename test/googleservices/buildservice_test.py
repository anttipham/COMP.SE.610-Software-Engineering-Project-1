""" Tests for google buildservice in googleservices. """

import googleservices.buildservice as buildservice
from environ import set_environ


class TestBuildGoogleService:
    """Tests for build_google_service function."""

    set_environ()

    def test_build_google_service(self):
        """Test that build_google_service returns a Resource object."""
        service = buildservice.build_google_service("calendar", "v3")
        assert service is not None
        assert service.__class__.__name__ == "Resource"
