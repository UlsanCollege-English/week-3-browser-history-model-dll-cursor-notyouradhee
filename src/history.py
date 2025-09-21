
### `/src/history.py` (starter)

class _N:
    __slots__ = ("url", "prev", "next")
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def current(self):
        return self.cur.url if self.cur else None

    def visit(self, url):
        new_node = _N(url)
        if not self.head:
            self.head = self.tail = self.cur = new_node
            return
        if self.cur != self.tail:
            nxt = self.cur.next
            while nxt:
                tmp = nxt.next
                nxt.prev = nxt.next = None
                nxt = tmp
            self.cur.next = None
            self.tail = self.cur
        self.cur.next = new_node
        new_node.prev = self.cur
        self.tail = new_node
        self.cur = new_node

    def back(self, steps=1):
        while steps > 0 and self.cur and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.current()

    def forward(self, steps=1):
        while steps > 0 and self.cur and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.current()
