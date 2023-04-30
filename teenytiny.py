from flask import Flask, request, send_file
from lex import *
from emit import *
from parse import *
import sys

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_source():
    print("Teeny Tiny Compiler")

    source = request.data.decode('utf-8')

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    
    return send_file("out.c")

if __name__ == '__main__':
    app.run(debug=True)