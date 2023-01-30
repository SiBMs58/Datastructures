"""
    Implementatie van een 2-3-4 boom.
"""

class treeItem:
    def __init__(self, keys=[], vals=[]):
        """
        -------------------------------------------------------
        Beschrijving:
            Initialiseert elke item/knoop van de boom, met zoeksleutels en waarden
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Een item/knoop van de boom is aangemaakt
        -------------------------------------------------------
        """
        self.keys = keys
        self.vals = vals
        self.children = []

    def isLeaf(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een knoop/treeItem een blad is
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Er wordt een boleaanse terug gegeven indien de knoop
            een blad is
        -------------------------------------------------------
        """
        if len(self.children) == 0:
            return True
        else:
            return False

def createTreeItem(key,val):
    """
    -------------------------------------------------------
    Beschrijving:
        Creëert een TreeItemType, dit is het type van de elementen in de 2-3-4.
    -------------------------------------------------------
    Preconditie:
        /
    Postconditie:
        Een lege treeItem is aangemaakt
    -------------------------------------------------------
    """
    return treeItem(key, val)

class TwoThreeFourTree:
    def __init__(self, order=3):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege 2-3-4 boom
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Er is een 2-3-4 boom aangemaakt
        -------------------------------------------------------
        """
        self.root = None
        self.order = order

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een 2-3-4 boom leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de 2-3-4 boom leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.root is None:
            return True
        else:
            return False

    def searchTreeItem(self, treeItem, searchKey):
        """
        -------------------------------------------------------
        Beschrijving:
            Zoekt in de 2-3-4 boom naar het item met searchKey als zoeksleutel
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De knoop wodt teruggeven
        -------------------------------------------------------
        """
        if treeItem.isLeaf():
            return treeItem

        for i, k in enumerate(treeItem.keys):
            if searchKey < k:
                return self.searchTreeItem(treeItem.children[i], searchKey)

        return self.searchTreeItem(treeItem.children[-1], searchKey)

    def searchParent(selfself, treeItem, child):
        if treeItem.is_leaf():
            return None

        if child in treeItem.children:
            return treeItem

        for c in treeItem.children:
            parent = treeItem.searchParent(c, child)
            if parent:
                return parent

        return None

    def insertItem(self, newItem):
        key = newItem.keys
        node = self.searchTreeItem(self.root, key)
        node.keys.append(key)
        node.keys.sort()
        if len(node.keys) > 3:
            self.split(node)
    def split(self, node):
        # Kijkt eerst of de lengte even of oneven is - Als er twee si- blings een item kunnen uitlenen, kies je voor de linkse.
        if (len(node.keys) % 2 == 0):
            m = (len(node.keys) // 2) - 1
        else:
            m = len(node.keys) // 2
        left_keys = node.keys[:m]
        right_keys = node.keys[m:]

        if node.is_leaf():
            left_children = []
            right_children = []
        else:
            left_children = node.children[:m + 1]
            right_children = node.children[m + 1:]

        left = treeItem(left_keys, left_children)
        right = treeItem(right_keys, right_children)

        if node is self.root:
            self.root = treeItem([node.keys[m]], [left, right])
        else:
            parent = self._find_parent(self.root, node)
            index = parent.children.index(node)

            parent.keys.insert(index, node.keys[m])
            parent.keys.sort()
            parent.children[index] = left
            parent.children.insert(index + 1, right)

            if len(parent.keys) > 3:
                self._split_node(parent)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode stelt een 2-3-4 boom voor als een dict.
        -------------------------------------------------------
        Preconditite:
            De 2-3-4 boom mag niet leeg zijn
        Postconditions:
            De waarden van de zoeksleutels worden weergegeven in een dict.
        -------------------------------------------------------
        """
        def save_bst(node):
            data = {}
            # Kijkt of node niet leeg is
            if node is None:
                return None
            # Zet de root van elke boom gelijk aan de zoeksleutel van elke node
            data['root'] = node.keys
            # Kijkt of we al in een blad zitten al dan niet
            if len(node.children) > 1:
                data['children'] = []
                for child in node.children:
                    data['children'].append(save_bst(child))
            return data
        # Slaag elk node op in de dict. beginnen van de root
        return save_bst(self.root)

    def load(self, data):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode laad een dict. in als een 2-3-4 boom
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De dict. wordt ingeladen als een 2-3-4 boom, met voor elke
            treeItem de key gelijk aan de val
        -------------------------------------------------------
        """
        def load_bst(dict):
            # Checkt of de dict niet leeg is
            if dict is None:
               return None
            # Maakt een treeItem aan voor de root, met als key en val dezelfde waarden
            treeItem = createTreeItem(dict['root'], dict['root'])
            # Kijk of er kinderen zijn
            if 'children' in dict:
                if dict['children'] is not None:
                    for child in dict['children']:
                        treeItem.children.append(load_bst(child))
                else:
                    None
            return treeItem
        # Zet de ingeladen BST gelijk aan onze self.root
        self.root = load_bst(data)


if __name__ == "__main__":
    t = TwoThreeFourTree()
    print(t.isEmpty()) # --> True
    #print(t.insertItem(createTreeItem(8,8))) # --> True
    #print(t.insertItem(createTreeItem(5,5))) # --> True
    #print(t.insertItem(createTreeItem(10,10))) # --> True
    #print(t.insertItem(createTreeItem(15,15))) # --> True
    #print(t.isEmpty()) # --> False
    #print(t.retrieveItem(5)[0])
    #print(t.retrieveItem(5)[1])
    #t.inorderTraverse(print)
    print(t.save())
    t.load({'root': [10],'children':[{'root':[5]},{'root':[11]}]})
    print(t.save())
    t.insertItem(createTreeItem(15,15))
    #print(t.deleteItem(0))
    print(t.save())
    #print(t.deleteItem(10))
    #print(t.save())