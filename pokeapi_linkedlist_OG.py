from LinkedList import LinkedList

class Pokemon:
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.weight = None
        self.types = []
        self.image = ''
        self.pokemon_api_call()
        
    def pokemon_api_call(self):
        response_object = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response_object.ok:
            poke_info = response_object.json()
            self.name = poke_info['name']
            self.abilities = poke_info['abilities']
            self.weight = poke_info['weight']
            self.types = poke_info['types']
            self.image = poke_info['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = poke_info['sprites']['front_default']
            setattr(self, 'species_url', poke_info['species']['url'])
        else:
            print(f'Error: status code {response_object.status_code}')
            
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def display_pokemon_info(self):
        print(f'{self.name} Weight: {self.weight}')
        print('Types:', end=' ')
        for poke_type in self.types:
            print(poke_type['type']['name'], end= ' ')
        print('\nAbilities:', end=' ')
        for ability in self.abilities:
            print(ability['ability']['name'],end=' ')
        # self.display_image()
        
    # def display_image(self, width=150):
    #     display(Image(self.image,width=width))

    def get_evolution_chain(self):
        res = get(self.species_url)
        if res.ok:
            data = res.json()
            self.store_evo_chain(data['evolution_chain']['url'])
            
            

    def store_evo_chain(self, evo_chain_url):
      print(evo_chain_url)
      res = get(evo_chain_url)
      if res.ok:
        print('success')
        data = res.json()
        current_dict = data['chain']
        lst = None
        while current_dict['evolves_to']:
            if not lst:
              lst = LinkedList(current_dict['species']['name'])
            else:
                lst.append_node(current_dict['species']['name'])
            current_dict = current_dict['evolves_to'][0]
        lst.append_node(current_dict['species']['name'])
      setattr(self,'evo_chain',lst)
      