from flask import Blueprint, request, jsonify

example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/api/v1/hello')
def get_hello():
    lang = request.args.get('user')
    return jsonify(message=f"{lang} ! Hello",
                   category="success",
                   data=lang,
                   status=200)