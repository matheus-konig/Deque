class Deque:
    '''Instancia a Deque com a opção de impor ou não um limite de elementos.'''
    def __init__(self, max_size = None):
        self._elements = []
        self._max_size = max_size

    def size(self):
        '''Retorna a quantidade de elementos presentes na lista em INT.'''
        return len(self._elements)

    def is_empty(self):
        '''Retorna True se a lista estiver vazia, caso contrário retorna False. '''
        return self.size() == 0
    

    def is_full(self):
        '''Retorna True se o tamanho da Deque tiver alcançado ou excedido o limite. 
        Caso não tenha chego ou não possua limite retorna False. '''
        if self._max_size is None:
            return False
        
        return self.size() >= self._max_size

    def clear(self):
        '''Remove todos os elementos da lista.'''
        self._elements.clear()

    def insert_first(self, element):
        '''Adiciona um elemento no começo da lista. Se a Deque já estiver cheia causa um Overflow Error'''
        if self.is_full(): 
            raise OverflowError("Não foi possível adicionar o elemento, pois o limite da Deque foi atingido.")
        self._elements.insert(0, element) # parâmetros: insert(indice, elemento); nesse caso o indice 0 representa a primeira posição na lista.

    def insert_last(self, element):
        '''Adiciona um elemento no final da lista. Se a Queue já estiver cheia causa um Overflow Error'''
        if self.is_full():
            raise OverflowError("Não foi possível adicionar o elemento, pois o limite da Deque foi atingido.")
        self._elements.append(element)
    

    def remove_first(self): 
        '''Remove o primeiro elemento da lista. Se já estiver vazia causa um Index Error.'''
        if self.is_empty():
            raise IndexError("Não é possível remover elementos da lista, pois ela já está vazia.")
        
        removed_element = self._elements.pop(0) 
        return removed_element


    def remove_last(self):
        '''Remove o último elemento da lista. Se já estiver vazia causa um Index Error.'''
        if self.is_empty():
            raise IndexError("Não é possível remover elementos da lista, pois ela já está vazia.")
        
        removed_element = self._elements.pop() # parâmetros: pop(posicao); quando não especificada a posição padrão é -1, que se refere ao último elemento.
        return removed_element

    def first(self):
        '''Retorna o valor do primeiro elemento da lista. Se estiver vazia causa um Index Error.'''
        if self.is_empty():
            raise IndexError("Não há elementos na lista para visualizar.")
        return self._elements[0]

    def last(self):
        '''Retorna o valor do último elemento na lista. Se estiver vazio causa um Index Error.'''
        if self.is_empty():
            raise IndexError("Não há elementos na lista para visualizar.")
        return self._elements[-1] # -1 retorna o último elemento.



if __name__ == "__main__" :
    
    deque = Deque(3)

    print("INICIANDO DEQUE COM LIMITE DE TRÊS ELEMENTOS\n")

    print(f"Deque está vazia? {deque.is_empty()}")

    print(f"Tamanho atual: {deque.size()}")

    print("\nInserindo item ao final da Deque...")
    deque.insert_last("Item B")
    print(f"{deque.last()} inserido com sucesso!")

    print("\nInserindo item no ínicio da Deque...")
    deque.insert_first("Item A")
    print(f"{deque.first()} inserido com sucesso!")

    print("\nInserindo novamente um item ao final da Deque...")
    deque.insert_last("Item C")
    print(f"{deque.last()} Inserido com sucesso!")

    try: 
        print("\nInserindo novamente um item ao final da Deque...")
        deque.insert_last("Item D")
    except OverflowError as erro_limit:
        print(f"Erro: {erro_limit}")

    print(f"\nTamanho atual: {deque.size()}")

    print(f"Primeiro item da lista: {deque.first()}")
    
    print(f"Último item da lista: {deque.last()}")

    print("\nRemovendo o item no início da Deque...")
    removido_inicio = deque.remove_first()
    print("Item removido com sucesso!")

    print(f"\nPrimeiro item da lista: {deque.first()}")

    print("\nRemovendo o item no final da Deque...")
    removido_final = deque.remove_last()
    print("Item removido com sucesso!")

    print(f"\nÚltimo item da lista: {deque.last()}")


    print(f"\nDeque está vazia? {deque.is_empty()}")

    print(f"Tamanho atual: {deque.size()}")

    print("\nRemovendo o último elemento presente na Deque")
    removido_inicio = deque.remove_first()
    print("Item removido com sucesso!")

    print(f"\nDeque está vazia? {deque.is_empty()}")

    try: 
            print("\nRemovendo o item no início da Deque...")
            deque.remove_first()
    except IndexError as erro_notfound:
        print(f"Erro: {erro_notfound}")