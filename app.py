from pc import PlayerCharacter
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/assh-character", methods=["GET"])
def assh_char():
    posted_data = request.get_json()
    # name = posted_data['name']
    # return jsonify(" Hope you are having a good time " +  name + "!!!")

    player_character = PlayerCharacter(magician_spell_src='dying_earth')
    return player_character.to_dict()


if __name__=='__main__':
   app.run(debug=True)
