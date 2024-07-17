import sys
from collections import defaultdict
from collections import deque

class MultiValueDictionary:
    def __init__(self):
        self.dic = defaultdict(set)
        self.log = deque()

    def log_command(self, command) -> None:
        if len(self.log) >= 10:
            self.log.popleft()
        self.log.append(command)
    
    #KEYS: Returns all the keys in the dictionary. Order is not guaranteed.
    def keys(self) -> str:
        self.log_command("KEYS")
        if not self.dic:
            return "(empty set)"
        else:
            i = 1
            ret = ""
            for k, _ in self.dic.items():
                ret += (f"{i}) {k}\n")
                i += 1
            return ret.rstrip()
    
    #MEMBERS: Returns the collection of strings for the given key. Return order is not guaranteed. Returns an error if the key does not exists.
    #Notes: Added return (empty set) to align with theme of sample.
    def members(self, key) -> str:
        self.log_command("MEMBERS " + key)
        if key not in self.dic:
            return ") ERROR, key does not exist."
        elif not self.dic[key]:
            return "(empty set)"
        else:
            i = 1
            ret = ""
            for v in self.dic[key]:
                ret += (f"{i}) {v}\n")
                i += 1
            return ret.rstrip()

    #ADD: Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
    def add(self, key, value) -> str:
        self.log_command("ADD " + key + " " + value)
        if value in self.dic[key]:
            return ") ERROR, member already exists for key"
        else:
            self.dic[key].add(value)
            return ") Added"

    #REMOVE: Removes a member from a key. If the last member is removed from the key, the key is removed from the dictionary. If the key or member does not exist, displays an error.
    #Notes: If value of key is already empty, the key will not be removed.
    def remove(self, key, value) -> str:
        self.log_command("REMOVE " + key + " " + value)
        if key not in self.dic:
            return ") ERROR, key does not exist"
        elif value not in self.dic[key]:
            return ") ERROR, member does not exist"
        else:
            self.dic[key].remove(value)
            if not self.dic[key]:
                self.dic.pop(key)
            return ") Removed"

    #REMOVEALL: Removes all members for a key and removes the key from the dictionary. Returns an error if the key does not exist.
    def remove_all(self, key) -> str:
        self.log_command("REMOVEALL " + key)
        if key not in self.dic:
            return ") ERROR, key does not exist"
        else:
            self.dic.pop(key)
            return ") Removed"

    #CLEAR: Removes all keys and all members from the dictionary.
    def clear(self) -> str:
        self.log_command("CLEAR")
        self.dic = defaultdict(set)
        return ") Cleared"

    #KEYEXISTS: Returns whether a key exists or not.
    def key_exists(self, key) -> str:
        self.log_command("KEYEXISTS " + key)
        if key in self.dic:
            return ") true"
        else:
            return ") false"

    #MEMBEREXISTS: Returns whether a member exists within a key. Returns false if the key does not exist.
    #Notes: Separated the state for if key does not exist and if key exists but value does not exist.
    def member_exists(self, key, value) -> str:
        self.log_command("MEMBEREXISTS " + key + " " + value)
        if key not in self.dic:
            return ") false"
        elif value in self.dic[key]:
            return ") true"
        else:
            return ") false"

    #ALLMEMBERS: Returns all the members in the dictionary. Returns nothing if there are none. Order is not guaranteed.
    #Notes to self: check for only key, no value
    def all_members(self) -> str:
        self.log_command("ALLMEMBERS")
        if not self.dic:
            return "(empty set)"
        else:
            i = 1
            ret = ""
            for _, values in self.dic.items():
                for v in values:
                    ret += (f"{i}) {v}\n")
                    i += 1
            if i == 1:
                return "(empty set)"
            else:
                return ret.rstrip()

    #ITEMS: Returns all keys in the dictionary and all of their members. Returns nothing if there are none. Order is not guaranteed.
    def items(self) -> str:
        self.log_command("ITEMS")
        if not self.dic:
            return "(empty set)"
        else:
            empty = True
            ret = ""
            for key, values in self.dic.items():
                for v in values:
                    ret += (f"{key}: {v}\n")
                    empty = False
            if empty:
                return "(empty set)"
            else:
                return ret.rstrip()

    #HISTORY: Returns last 10 successful calls to MVD.
    def history(self) -> str:
        ret = ""
        i = 1
        if not self.log:
            return "(empty list)"
        for h in self.log:
            ret += (f"{i}) {h}\n")
            i += 1
        return ret.rstrip()

#HELP: Offers help for struggling folks.

#EXIT: Quits program.

def main():
    try:
        mvd = MultiValueDictionary()
        while True:
            command = input("> ").strip().split()
            if not command:
                continue
            action = command[0].upper()
            if action == "KEYS" and len(command) == 1:
                print(mvd.keys())
            elif action == "MEMBERS" and len(command) == 2:
                print(mvd.members(command[1]))
            elif action == "ADD" and len(command) == 3:
                print(mvd.add(command[1], command[2]))
            elif action == "REMOVE" and len(command) == 3:
                print(mvd.remove(command[1], command[2]))
            elif action == "REMOVEALL" and len(command) == 2:
                print(mvd.remove_all(command[1]))
            elif action == "CLEAR" and len(command) == 1:
                print(mvd.clear())
            elif action == "KEYEXISTS" and len(command) == 2:
                print(mvd.key_exists(command[1]))
            elif action == "MEMBEREXISTS" and len(command) == 3:
                print(mvd.member_exists(command[1], command[2]))
            elif action == "ALLMEMBERS" and len(command) == 1:
                print(mvd.all_members())
            elif action == "ITEMS" and len(command) == 1:
                print(mvd.items())
            elif action == "HISTORY" and len(command) == 1:
                print(mvd.history())
            elif action == "HELP" and len(command) == 1:
                print(r"Here is a helping hand ¯\_      (ツ)_/¯")
            elif action == "EXIT" and len(command) == 1:
                print("Bye Bye")
                break
            else:
                print("Invalid command")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")

if __name__ == "__main__":
    main()