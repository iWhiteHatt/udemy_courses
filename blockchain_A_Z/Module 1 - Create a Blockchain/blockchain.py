import datetime
import hashlib
import json
from flask import Flask, jsonify

#--------------------------------------- Module 1 - Create a Blockchain

class Blockchain:

    def _init_(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {}

#--------------------------------------- Part 2 - Mining our Blockchain

