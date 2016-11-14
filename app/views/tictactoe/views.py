from copy import deepcopy

import dill
from flask import render_template, jsonify, session

from app import app
from tictactoe import TicTacToe
from alphabeta import minimax_with_alphabeta


@app.route('/tictactoe')
def tictactoe_root():
    game = TicTacToe()
    session['game'] = dill.dumps(game)
    session['ai_player'] = None
    session.modified = True
    return render_template('tictactoe/index.html')


@app.route('/tictactoe/choose/<symbol>')
def tictactoe_choice(symbol):
    if symbol not in ['O', 'X']:
        return 'Error'
    session['ai_player'] = 'B' if symbol == 'O' else 'A'
    session.modified = True
    # print 'The player for AI is -', session['ai_player']
    return session['ai_player']


@app.route('/tictactoe/move/<pos>')
def tictactoe_move(pos):
    # print 'User moved -', pos
    pos = int(pos)

    game = dill.loads(session['game'])
    game.move(pos)
    # game.display()
    if game.status != None:
        x = 'ai' if game.winner == session['ai_player'] else 'user'
    else:
        x = ''

    session['game'] = dill.dumps(game)
    session.modified = True
    return jsonify({
        'move': pos,
        'status': game.status,
        'winner': x,
        'winning_pos': game.winning_pos
    })


@app.route('/tictactoe/move_minimax')
def tictactoe_minimax():
    game = dill.loads(session['game'])

    pos = int(minimax_with_alphabeta(
        deepcopy(game), session['ai_player'],
        float('-inf'), float('inf'))[0])
    game.move(pos)
    # game.display()

    if game.status != None:
        x = 'ai' if game.winner == session['ai_player'] else 'user'
    else:
        x = ''

    session['game'] = dill.dumps(game)
    return jsonify({
        'move': pos,
        'status': game.status,
        'winner': x,
        'winning_pos': game.winning_pos
    })
