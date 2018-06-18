from rest_framework import authentication
from rest_framework import exceptions
import json
from six.moves.urllib.request import urlopen
from jose import jwt


AUTH0_DOMAIN = "zerrtechdev.auth0.com"
API_AUDIENCE = "https://zerrtechdev.auth0.com/api/v2/"
ALGORITHMS = ["RS256"]


def get_auth_token(request):
    auth = request.META.get("HTTP_AUTHORIZATION")
    auth_parts = auth.split()

    if auth_parts[0].lower() != "bearer":
        raise exceptions.AuthenticationFailed("Authorization header must start with")
    elif len(auth_parts) == 1:
        raise exceptions.AuthenticationFailed("Token not found")
    elif len(auth_parts) > 2:
        raise exceptions.AuthenticationFailed("Authorization header must be")

    return auth_parts[1]


def validate_token(request):
    try:
        token = get_auth_token(request)
        jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://" + AUTH0_DOMAIN + "/"
                )
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed("Signature error")
            except jwt.JWTClaimsError as e:
                print(e)
                raise exceptions.AuthenticationFailed("Claims Error")
            except Exception as e:
                print(e)
                raise exceptions.AuthenticationFailed("JWT Exception")

        return payload
    except Exception:
        raise exceptions.AuthenticationFailed("Authentication Failed")


class Auth0Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        validate_token(request)

        return None, None
