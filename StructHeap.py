"""
    Implementatie van een Linked Based Heap
"""
class heapItem:
    def __init__(self, key=None):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een heapItemType, dit is het type van de elementen
            in de heap. Een element van dit type heeft een zoeksleutel
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Een heapItem is aangemaakt
        -------------------------------------------------------
        """
        self.left = None
        self.right = None
        self.key = key
        self.parent = None

    """
    -------------------------------------------------------
    Beschrijving:
        Alle helpfuncties die worden gebruikt voor het 
        bewerkingscontract te kunnen nakom.
    -----
    """

    def isLeaf(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een heapItem een blad is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als het heapItem een blad is, zo niet False.
        -------------------------------------------------------
        """
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een heapItem leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als het heapItem leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.key == None:
            return True
        else:
            return False

    def swap(self, other):
        """
        -------------------------------------------------------
        Beschrijving:
            Wisselt 2 heap items van plaats
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De 2 heap items werden van plaats verwisselt
        -------------------------------------------------------
        """
        heapItemKey = self.key
        otherKey = other.key
        self.key = otherKey
        other.key = heapItemKey

    def fix(self, lastHeapItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze functie is verantwoordelijk voor het behouden van de heap-eigenschappen
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De heap bevat alle heap-eigenschappen
        -------------------------------------------------------
        """
        if lastHeapItem.parent is not None:
            lastHeapItem.parent.removeChild(lastHeapItem)
        newTreeItem = heapItem(lastHeapItem.key)
        newTreeItem.parent = self
        if self.left is None:
            self.left = newTreeItem
        elif self.right is None:
            self.right = newTreeItem

    def getLastHeapItem(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Zoek naar het meest rechtse item onderaan.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Het laatste heapItem wordt ge returned
        -------------------------------------------------------
        """
        if self.isLeaf():
            return self
        if self.right:
            return self.right.getLastHeapItem()
        else:
            return self.left.getLastHeapItem()

    def removeChild(self, child):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijderd een kind
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Het kind werd verwijderd
        -------------------------------------------------------
        """
        if child == self.left:
            self.left = None
        else:
            self.right = None

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def heapifyUp(self, operator):
        """
        -------------------------------------------------------
        Beschrijving:
            Wordt gebruik na het invoegen van een item in de heap, om
            de heap zijn heap-eigenschappen te laten behouden
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De heap bevat alle eigenschappen van een heap
        -------------------------------------------------------
        """
        if self.parent is not None:
            if operator(self, self.parent) == self:
                self.swap(self.parent)
                self.parent.heapifyUp(operator)

    def heapifyDown(self, operator):
        """
        -------------------------------------------------------
        Beschrijving:
            Wordt gebruik na het invoegen van een item in de heap, om
            de heap zijn heap-eigenschappen te laten behouden
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De heap bevat alle eigenschappen van een heap
        -------------------------------------------------------
        """
        if self.left is not None:
            if operator(self.left, self) == self.left:
                self.swap(self.left)
                self.left.heapifyDown(operator)
        if self.right is not None:
            if operator(self.right, self) == self.right:
                self.swap(self.right)
                self.right.heapifyDown(operator)

    def insertComplete(self, val):
        newNode = heapItem(val)
        newNode.parent = self
        if self.left is None:
            self.left = newNode
        elif self.right is None:
            self.right = newNode
        elif self.left is not None:
            return self.left.insertComplete(val)
        elif self.right is not None:
            return self.right.insertComplete(val)
        return newNode


class Heap:
    def __init__(self,maxHeap=True):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege min-/ max-heap a.d.h.v. de opgegeven
            :param maxHeap
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Er is een heap aangemaakt
        -------------------------------------------------------
        """
        self.root = heapItem()
        self.maxHeap = maxHeap

    def get_comparison_operator(self):
        return max if self.maxHeap else min

    def heapIsEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een heap leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de BST leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.root.isEmpty():
            return True
        else:
            return False

    def heapInsert(self, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Voegt newItem toe aan eenheap met items met unieke zoeksleutels
            verschillend van de zoeksleutel van newItem
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een heap aangemaakt zijn
        Postconditions:
            Het newItem wordt aan de heap toegevoegd, gesorteerd
            volgens het type van de heap.
        -------------------------------------------------------
        Return : True geeft weer dat het toevoegen gelukt is anders False
        -------------------------------------------------------
        """
        if self.heapIsEmpty():
            self.root.key = newItem
            return True
        newNode = self.root.insertComplete(newItem)
        comparisonOperator = self.get_comparison_operator()
        newNode.heapifyUp(comparisonOperator)
        return True
    def heapDelete(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijderd rootItem uit de heap
            Het element met de grootste zoeksleutel (bij een max-heap) of
            het element met de kleinste zoeksleutel (bij een min-heap)
            wordt verwijderd.
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een heap aangemaakt zijn
        Postconditions:
            Het root wordt uit de heap verwijderd, afhankelijk van max of min heap
        -------------------------------------------------------
        Return : True geeft weer dat het verwijderen gelukt is anders False
        -------------------------------------------------------
        """
        if self.heapIsEmpty():
            return (None, False)
        rootItem = self.root.key
        lastItem = self.root.getLastHeapItem()
        self.root.swap(lastItem)
        if lastItem.parent is not None:
            lastItem.parent.removeChild(lastItem)
        comparisonOperator = self.get_comparison_operator()
        self.root.heapifyDown(comparisonOperator)
        if lastItem.parent is not None:
            temp = self.root.getLastHeapItem().parent
            l = temp.left
            r = temp.right
            comparisonOperator = self.get_comparison_operator()
            if l == None:
                lastItem.parent.fix(r)
            elif r == None:
                lastItem.parent.fix(l)
            elif comparisonOperator(l.key, r.key) == l.key:
                lastItem.parent.fix(r)
            elif comparisonOperator(l.key, r.key) == r.key:
                lastItem.parent.fix(l)
                temp.left = r
                temp.right = None
        return (rootItem, True)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode stelt een heap voor als een dict.
        -------------------------------------------------------
        Preconditite:
            De heap mag niet leeg zijn
        Postconditions:
            De waarden van de zoeksleutels worden weergegeven in een dict.
        -------------------------------------------------------
        """
        def save_heap(heapItem):
            data = {}
            if heapItem is None:
                return None
            data['root'] = heapItem.key
            if heapItem.left is not None or heapItem.right is not None:
                data['children'] = []
                if heapItem.left is not None:
                    data['children'].append(save_heap(heapItem.left))
                else:
                    data['children'].append(None)
                if heapItem.right is not None:
                    data['children'].append(save_heap(heapItem.right))
                else:
                    data['children'].append(None)
            return data
        return save_heap(self.root)

    def load(self, data):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode laad een dict. in als een heap
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De dict. wordt ingeladen als een heap, met voor elke heapItem
            de key gelijk aan de val van de 'root' key
        -------------------------------------------------------
        """
        def load_bst(dict, parent):
            # Checkt of de dict niet leeg is
            if dict is None:
               return None
            # Maakt een knoop aan voor de root, met als key de key die de root key heeft
            node = heapItem(dict['root'])
            node.parent = parent
            # Kijk of er kinderen zijn
            if 'children' in dict:
                # Kijkt op linker kinderen
                if dict['children'][0] is not None:
                    node.left = load_bst(dict['children'][0], node)
                else:
                    None
                # Kijkt op rechter kinderen
                if len(dict['children']) > 1 and dict['children'][1] is not None:
                    node.right = load_bst(dict['children'][1], node)
                else:
                    None
            return node
        # Zet de ingeladen BST gelijk aan onze self.root
        self.root = load_bst(data, None)

if __name__ == "__main__":
    """t = Heap()
    print(t.heapIsEmpty())
    print(t.heapDelete()[1])
    print(t.heapInsert(5))
    print(t.heapInsert(8))
    print(t.heapIsEmpty())
    print(t.save())
    t.load({'root': 10, 'children': [{'root': 5}, None]})
    t.heapInsert(15)
    print(t.save())
    result = t.heapDelete()
    print(result[0])
    print(result[1])
    print(t.save())"""
    # Vraag 3
    t = Heap()
    t.heapInsert(2)
    t.heapInsert(3)
    t.heapInsert(1)
    print(t.save())
    t.heapInsert(5)
    print(t.save())
    t.heapInsert(9)
    print(t.save())
    """# Vraag 4
    t = Heap()
    t.load({'root': 9, 'children': [{'root': 5, 'children': [{'root': 2}, {'root': 3}]}, {'root': 1}]})
    result = t.heapDelete()
    print(t.save())
    result = t.heapDelete()
    print(t.save())"""
    """# Vraag 5
    t = Heap()
    t.load({'root': 3, 'children': [{'root': 2}, {'root': 1}]})
    t.heapInsert(5)
    t.heapInsert(4)
    result = t.heapDelete()
    print(t.save())"""
    """t = Heap()
    t.heapInsert(2)
    t.heapInsert(3)
    t.heapInsert(5)
    t.heapInsert(6)
    t.heapInsert(9)
    t.heapInsert(10)
    print(t.save())
    t.heapDelete()
    print(t.save())"""