from collections import deque


def search_queue(graph, dq, right, searched=[]):
    def addnextlevel(dq, node):
        next_level = graph.get(node)
        if next_level:
            dq += next_level

    if dq:
        node = dq.popleft()
        if node in searched:
            return search_queue(graph, dq, right, searched)
        else:
            if right(node):
                print("This is the appropriate node:", node)
                return True
            else:
                searched.append(node)
                addnextlevel(dq, node)
                return search_queue(graph, dq, right, searched)
    else:
        print("We can't find the appropriate node")
        return False


def breath_first_search_demo():
    def right(node):
        return node[-1] == 'm'

    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    dq = deque(['you'])
    print(search_queue(graph, dq, right))


breath_first_search_demo()
