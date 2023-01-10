# flask-swagger-api
Flask based API using Swagger documentation

# References
[rest-apis-flask.teclado.com](https://rest-apis-flask.teclado.com/)

# Secure an endpoint
add security options right after path
```
  "paths": {
    "/item/{item_id}": {
      "get": {
        "security": [
          {
            "bearerAuth": []
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Item"
                }
              }
            }
          },
```
