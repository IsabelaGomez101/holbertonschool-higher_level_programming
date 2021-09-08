#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for nmway in dir(hidden_4):
        if nmway[:2] != "__":
            print(nmway)
