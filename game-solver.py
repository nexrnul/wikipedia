from queue import Queue
import wikipediaapi
import time

user_agent = "MsOrret'sWikipediaGame/1.0 (orret.deborah@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")

# passes wikipedia page and returns a list of all pages linked on starting page
def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        
    return links_list

#IN CLASS: Finish the definition of the wikipedia_game_solver using a Breadth-First-Search Traversal
def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()

    visited = []
    queue = Queue()
    path = []
    parent = {}

    queue.put(start_page.title)
    visited.append(start_page.title)
#breadth first search traversal
    while not queue.empty():
        current_title = queue.get()

        if current_title == target_page.title:
            break

        visited.append(current_title)
        current_page = wiki_wiki.page(current_title)
        next_level = fetch_links(current_page)
#solution to multiple nodes being prevelant (speeds up process)
        for node in next_level:
            if node not in visited:
                queue.put(node)
                parent[node] = current_title
#determination             
    child = target_page.title
    while child != start_page.title:
        path.append(child)
        child = parent[child]
    path.append(start_page.title)
    path.reverse()
    end_time = time.time()    
    print("this traversal took", end_time-start_time, "seconds to run")

    return path
    

# results
start_page = wiki_wiki.page('Ogdoad (Gnosticism)')
target_page = wiki_wiki.page('Seven heavens')
path = wikipedia_game_solver(start_page, target_page)
print("you traveled from: %s" % start_page.title)
print("all the way to: %s" % target_page.title)
print("brief summary: %s" % target_page.summary[0:20])
print("shortest pathway:", path)

