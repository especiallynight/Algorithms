import sys


class Trie:
    def __init__(self) -> None:
        """Создаёт пустое префиксное дерево."""
        self.children: list[list[int]] = [[-1] * 26]
        self.prefix_count: list[int] = [0]
        self.word_count: list[int] = [0]

    def add(self, word: str) -> None:
        """Добавляет слово и обновляет счётчики префиксов."""
        node: int = 0
        self.prefix_count[node] += 1

        for char in word:
            index: int = ord(char) - ord('a')

            if self.children[node][index] == -1:
                self.children[node][index] = len(self.children)
                self.children.append([-1] * 26)
                self.prefix_count.append(0)
                self.word_count.append(0)

            node = self.children[node][index]
            self.prefix_count[node] += 1

        self.word_count[node] += 1

    def remove(self, word: str) -> None:
        """Удаляет одно вхождение слова."""
        node: int = 0
        path: list[int] = [0]

        for char in word:
            index: int = ord(char) - ord('a')
            node = self.children[node][index]
            path.append(node)

        self.word_count[node] -= 1

        for node in path:
            self.prefix_count[node] -= 1

    def count(self, prefix: str) -> int:
        """Считает слова с заданным префиксом."""
        node: int = 0

        for char in prefix:
            index: int = ord(char) - ord('a')
            node = self.children[node][index]

            if node == -1:
                return 0

        return self.prefix_count[node]


q: int = int(sys.stdin.buffer.readline())
trie = Trie()
results: list[str] = []

for _ in range(q):
    operation, word = sys.stdin.buffer.readline().decode().split()

    if operation == "ADD":
        trie.add(word)
    elif operation == "REMOVE":
        trie.remove(word)
    elif operation == "COUNT":
        results.append(str(trie.count(word)))

sys.stdout.write("\n".join(results))

