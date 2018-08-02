#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from diffiehellman.diffiehellman import DiffieHellman

alice = DiffieHellman(group=18, key_length=1024)
bob = DiffieHellman(group=18, key_length=1024)

alice.generate_public_key()  # automatically generates private key
bob.generate_public_key()

alice.generate_shared_secret(bob.public_key, echo_return_key=True)
bob.generate_shared_secret(alice.public_key, echo_return_key=True)
a = alice.shared_key
b = bob.shared_key
