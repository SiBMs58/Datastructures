"""
    Implementatie van een binaire zoekboom.
"""

class createTreeItem:
    def __init__(self, key, val):
        """
        -------------------------------------------------------
        Beschrijving:
        Creëert een TreeItemType, dit is het type van de elementen in de binaire zoekboom.
        Een element van dit type heeft een zoeksleutel, een value
        -------------------------------------------------------
        Preconditie:
        /
        Postconditie:
        Een lege treeItem is aangemaakt
        -------------------------------------------------------
        """
        self.left = None
        self.right = None
        self.key = key
        self.val = val


class BST:
    def __init__(self):
        """
        -------------------------------------------------------
        Beschrijving:
        Creëert een lege binaire zoekboom
        -------------------------------------------------------
        Preconditite:
        /
        Postconditions:
        Er is een BST aangemaakt
        -------------------------------------------------------
        """
        self.root = None

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een BST leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de BST leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.root is None:
            return True
        else:
            return False

    def search(self, binTree, searchKey):
        """
        -------------------------------------------------------
        Beschrijving:
            Zoekt in de binaire zoekboom binTree naar
            het item met searchKey als zoeksleutel
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Indien de searchKey al bestaat, wordt deze geturnd
            anders wordt er None terug gegeven dit betekent
            dat de opgegeven searchKey kan worden toegevoegd
        -------------------------------------------------------
        """
        if binTree is None:
            # Gezochte record is niet gevonden
            return None
        elif searchKey == binTree.key:
            # Gezochte record is gevonden
            return binTree
        elif searchKey < binTree.key:
            return self.search(binTree.left, searchKey)
        else:
            return self.search(binTree.right, searchKey)

    def searchTreeInsert(self, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Voegt newItem toe aan een binaire zoekboom met items met
            unieke zoeksleutels verschillend van de zoeksleutel van newItem
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een BST aangemaakt zijn
        Postconditions:
            Het newItem wordt aan de BST toegevoegd, gesorteerd volgens de key
        -------------------------------------------------------
        Return : True geeft weer dat het toevoegen gelukt is anders False
        -------------------------------------------------------
        """
        if self.root is None:
            self.root = newItem
            return True
        else:
            current = self.root
            while True:
                if newItem.key < current.key:
                    if current.left is None:
                        current.left = newItem
                        return True
                    else:
                        current = current.left
                elif newItem.key > current.key:
                    if current.right is None:
                        current.right = newItem
                        return True
                    else:
                        current = current.right
                else:
                    return False

    def searchTreeDelete(self, searchKey):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijdert een treeItem met de opgegeven searchKey uit de
            een binaire zoekboom met items met unieke zoeksleutels
            waarvan een van die zoeksleutels gelijk is aan de searchKey
        -------------------------------------------------------
        Preconditite:
            De opgegeven searchKey bestaat in de binaire zoekboom
        Postconditions:
            Het item dat overeen komt met de opgegeven searchKey
            wordt van de BST verwijderd, en de BST word opnieuw gesorteerd
        -------------------------------------------------------
        Return : True geeft weer dat het verwijderen gelukt is anders False
        -------------------------------------------------------
        """
        # Checkt op een lege boom
        if self.root is None:
            return False
        # Vind de te verwijderen knoop N, met het zoekalgoritme
        N = self.search(self.root, searchKey)
        # Zorg dat er wordt voldaan aan de preconditie
        if not N:
            # searchKey is niet gevonden
            return False
        # Speciaal geval indien we onze root moeten verwijderen
        if self.root.key == searchKey:
            #  2 mogelijkheden
            #  1. Root heeft 1 kind
            #  Kijkt of de root geen linker kind heeft
            if self.root.left is None:
                self.root = self.root.right
            # Kijkt of de root geen rechter kind heeft
            elif self.root.right is None:
                self.root = self.root.left
            # 2. Root heeft 2 kinderen
            else:
                # Voert een tree traversal uit, zoekt een treeItem met de kleinste key en deze wordt dan de root
                parent = self.root
                current = self.root.right
                while current.left:
                    parent = current
                    current = current.left
                # Zet treeItem uit de rechter deelboom van de root met kleinste key gelijk aan de root
                self.root.key = current.key
                self.root.val = current.val
                # Verwijderd het treeItem met de kleinste key
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            return True
        # Deze wordt later met onderstaande while loop gelijk gesteld aan de ouder van N
        parent = None
        # Word gebruikt om de ouder te zoeken
        current = self.root
        while current is not None and current.key != searchKey:
            parent = current
            if searchKey < current.key:
                current = current.left
            else:
                current = current.right
            if current is None:
                return False
        # Drie mogelijkheden:
        # 1. N is een blad
        if N.left is None and N.right is None:
            # Geval van de root
            if parent is None:
                self.root = None
            # Kijk of de te verwijderen boom in de linker boom zit van de ouder
            elif parent.left == N:
                parent.left = None
            # Checkt of de te verwijderen boom in de rechter boom zit van de ouder
            else:
                parent.right = None
            return True
        # 2. N heeft 1 kind
        elif N.left is None:
            # Geval van de root
            if parent is None:
                self.root = N.right
            # Geval linker boom
            elif parent.left == N:
                parent.left = N.right
            # Geval rechter boom
            else:
                parent.right = N.right
            return True
        elif N.right is None:
            # Geval van de root
            if parent is None:
                self.root = N.left
            # Geval linker boom
            elif parent.left == N:
                parent.left = N.left
            # Geval rechter boom
            else:
                parent.right = N.left
            return True
        # 3. N heeft 2 kinderen
        else:
            # searchKey moet voor N
            if searchKey < parent.key:
                # Zoek de inorder predecessor
                predecessorParent = N
                predecessor = N.left
                while predecessor.right:
                    predecessorParent = predecessor
                    predecessor = predecessor.right
                # Kopieer de sleutel van de inorder predecessor naar de sleutel van de N
                N.key = predecessor.key
                N.val = predecessor.val
                # Verwijder de inorder predecessor
                if predecessorParent.left == predecessor:
                    predecessorParent.left = predecessor.left
                else:
                    predecessorParent.right = predecessor.left
            # searchKey moet na N komen
            else:
                # Zoek de inorder successor
                successorParent = N
                successor = N.right
                while successor.left:
                    successorParent = successor
                    successor = successor.left
                # Kopieer de sleutel van de inorder successor naar de sleutel van de N
                N.key = successor.key
                N.val = successor.val
                # Verwijder de inorder successor
                if successorParent.right == successor:
                    successorParent.right = successor.right
                else:
                    successorParent.left = successor.right
            return True

    def searchTreeRetrieve(self, searchKey):
        """
        -------------------------------------------------------
        Beschrijving:
            Het item dat overeenkomt met de searchKey wordt opgehaald uit de BST
        -------------------------------------------------------
        Preconditite:
            De opgegeven searchKey bestaat in de binaire zoekboom
        Postconditions:
            Het item dat overeen komt met de opgegeven searchKey
            wordt teruggegeven
        -------------------------------------------------------
        Return : Als de searchKey is gevonden wordt er True geturnd,
        met de value die overeenkomt met de searchKey anders False
        -------------------------------------------------------
        """
        # Kijkt of de boom leeg is
        if self.root is None:
            # Gezochte record is niet gevonden
            return False
        # Zet het record eerst gelijk aan de root
        record = self.root
        # Loop voor het zoeken naar het item dat overeenkomt met de searchKey
        while record is not None:
            if record.key == searchKey:
                return (record.val, True)
            elif searchKey < record.key:
                record = record.left
            else:
                record = record.right
        return False

    def preorderTraverse(self, visit):
        """
        -------------------------------------------------------
        Beschrijving:
            Print de waarde van de BST uit volgende preorder volgorde
        -------------------------------------------------------
        Preconditite:
            De BST mag niet leeg zijn
        Postconditions:
            De waarden van de BST worden volgens preorder
            volgorde geprint
        -------------------------------------------------------
        """
        def preorderTraverseHelper(treeItem):
            if treeItem is not None:
                visit(treeItem.key)
                preorderTraverseHelper(treeItem.left)
                preorderTraverseHelper(treeItem.right)
        preorderTraverseHelper(self.root)

    def inorderTraverse(self, visit):
        """
        -------------------------------------------------------
        Beschrijving:
            Print de waarde van de BST uit volgende inorder volgorde
        -------------------------------------------------------
        Preconditite:
            De BST mag niet leeg zijn
        Postconditions:
            De waarden van de BST worden volgens inorder
            volgorde geprint
        -------------------------------------------------------
        """
        def inorderTraverseHelper(treeItem):
            if treeItem is not None:
                inorderTraverseHelper(treeItem.left)
                visit(treeItem.key)
                inorderTraverseHelper(treeItem.right)
        inorderTraverseHelper(self.root)

    def postorderTraverse(self, visit):
        """
        -------------------------------------------------------
        Beschrijving:
            Print de waarde van de BST uit volgende post order volgorde
        -------------------------------------------------------
        Preconditite:
            De BST mag niet leeg zijn
        Postconditions:
            De waarden van de BST Tree worden volgens postorder
            volgorde geprint
        -------------------------------------------------------
        """
        def postorderTraverseHelper(treeItem):
            if treeItem is not None:
                postorderTraverseHelper(treeItem.left)
                postorderTraverseHelper(treeItem.right)
                visit(treeItem.key)
        postorderTraverseHelper(self.root)



    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode stelt een BST voor als een dict.
        -------------------------------------------------------
        Preconditite:
            De BST mag niet leeg zijn
        Postconditions:
            De waarden van de zoeksleutels worden weergegeven in een dict.
        -------------------------------------------------------
        """
        def save_bst(treeItem):
            data = {}
            # Kijkt of treeItem niet leeg is
            if treeItem is None:
                return None
            # Zet de root van elke boom gelijk aan de zoeksleutel van elke treeItem
            data['root'] = treeItem.key
            # Kijkt of we al in een blad zitten al dan niet
            if treeItem.left is not None or treeItem.right is not None:
                # Als we nog niet in een blad zitten zijn er kinderen
                data['children'] = []
                # Kijk of er een linker kind is al dan niet
                if treeItem.left is not None:
                    data['children'].append(save_bst(treeItem.left))
                else:
                    data['children'].append(None)
                # Kijk of er een rechter kind is al dan niet
                if treeItem.right is not None:
                    data['children'].append(save_bst(treeItem.right))
                else:
                    data['children'].append(None)
            return data
        # Slaag elk treeItem op in de dict. beginnen van de root
        return save_bst(self.root)

    def load(self, data):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode laad een dict. in als een BST
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De dict. wordt ingeladen als een BST, met voor elke treeItem de key gelijk aan de val
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
                # Kijkt op linker kinderen
                if dict['children'][0] is not None:
                    treeItem.left = load_bst(dict['children'][0])
                else:
                    None
                # Kijkt op rechter kinderen
                if len(dict['children']) > 1 and dict['children'][1] is not None:
                    treeItem.right = load_bst(dict['children'][1])
                else:
                    None
            return treeItem
        # Zet de ingeladen BST gelijk aan onze self.root
        self.root = load_bst(data)


# Main:
if __name__ == "__main__":
    t = BST()
    print(t.isEmpty())
    print(t.searchTreeInsert(createTreeItem(8, 8)))
    print(t.searchTreeInsert(createTreeItem(5, 5)))
    print(t.isEmpty())
    print(t.searchTreeRetrieve(5)[0])
    print(t.searchTreeRetrieve(5)[1])
    t.inorderTraverse(print)
    print(t.save())
    t.load({'root': 10, 'children': [{'root': 5}, None]})
    t.searchTreeInsert(createTreeItem(15, 15))
    print(t.searchTreeDelete(0))
    print(t.save())
    print(t.searchTreeDelete(10))
    print(t.save())