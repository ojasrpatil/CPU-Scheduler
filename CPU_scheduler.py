'''
Author: Ojas Patil
KUID: 3042635
Date: Wednesday, February 24, 2022
Lab: lab03
Last modified: February 27, 2022
Purpose:
'''

from node_class import Node
from queue_class import Queue

def main():
    while True:
        try:
            read_file = open(str(input("File name: "))) #Asks for run file.
            queue = Queue()
            for line in read_file:
                words = line.split()
                index=0
                for word in words: #Detects key words.
                    if word == "START": #If keyword is start then add process to queue and make it call the function main.
                        node = Node(words[index+1])
                        queue.enqueue(node)
                        node.stack_calls.push("main")
                        print(f'{words[index+1]} added to queue')
                    elif word == "CALL": #If keyword is call then call the function given.
                        queue.peek_front().stack_calls.push(words[index+1])
                        removed_queue = queue.dequeue()
                        print(f'{removed_queue.entry} calls {words[index+1]}')
                        queue.enqueue(removed_queue)
                    elif word == "RETURN": #If keyword is return then return the current function being called, if all functions have been called then remove the process.
                        stack_top = queue.peek_front().stack_calls.peek()
                        print(f'{queue.peek_front().entry} returns from {stack_top.entry}')
                        if (stack_top.entry != "main"):
                            stack_top.pop()
                            queue.enqueue(queue.dequeue())
                        else:
                            print(f'{queue.peek_front().entry} process has ended')
                            queue.dequeue()
                    index+=1
            break
        except FileNotFoundError:
            print("File not found")

main()
