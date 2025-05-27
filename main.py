from typing import Optional

from fastapi import FastAPI

app = FastAPI()

darksouls2 = {
  "areas": [
    {
      "id": "things_betwixt",
      "name": "Things Betwixt",
      "description": "Área tutorial inicial, lar das Guardiãs do Fogo.",
      "connections": ["majula"],
      "required_items": {}
    },
    {
      "id": "majula",
      "name": "Majula",
      "description": "Hub central do jogo, conecta múltiplas regiões.",
      "connections": ["things_betwixt", "fofg", "htoh", "huntsmans_copse", "shaded_woods", "the_pit"],
      "required_items": {
        "fofg": None,
        "htoh": "Derrotar Dragonrider ou pagar 2000 almas para Licia",
        "huntsmans_copse": "Chave da Copse (vendida por Licia por 2000 almas)",
        "shaded_woods": "Emblema do Rei (King's Ring, adquirido mais tarde)",
        "the_pit": "Anel da Gata ou Feather Fall"
      }
    },
    {
      "id": "fofg",
      "name": "Forest of Fallen Giants",
      "description": "Floresta infestada de soldados mortos-vivos e gigantes.",
      "connections": ["cardinal_tower", "memory_of_jeigh", "majula"],
      "required_items": {
        "memory_of_jeigh": "Ashen Mist Heart"
      }
    },
    {
      "id": "cardinal_tower",
      "name": "Cardinal Tower",
      "description": "Fogueira central da floresta, próximo ao Pursuer.",
      "connections": ["fofg", "sinners_rise"],
      "required_items": {
        "sinners_rise": "Chave da Bastilha (Bastille Key) ou detonar parede"
      }
    },
    {
      "id": "htoh",
      "name": "Heide's Tower of Flame",
      "description": "Torre inundada com guerreiros de pedra e o Dragonrider.",
      "connections": ["no_mans_wharf", "majula"],
      "required_items": {
        "no_mans_wharf": None
      }
    },
    {
      "id": "no_mans_wharf",
      "name": "No-Man's Wharf",
      "description": "Porto escuro e abandonado, lar de piratas e monstros.",
      "connections": ["lost_bastille"],
      "required_items": {}
    },
    {
      "id": "lost_bastille",
      "name": "The Lost Bastille",
      "description": "Fortaleza infestada de Undead e Prisioneiros.",
      "connections": ["sinners_rise", "belfry_luna", "no_mans_wharf"],
      "required_items": {}
    },
    {
      "id": "belfry_luna",
      "name": "Belfry Luna",
      "description": "Torre opcional cheia de inimigos sinos e armadilhas.",
      "connections": ["lost_bastille"],
      "required_items": {}
    },
    {
      "id": "sinners_rise",
      "name": "Sinner's Rise",
      "description": "Fortaleza sombria onde reside a Pecadora Perdida.",
      "connections": ["lost_bastille"],
      "required_items": {}
    },
    {
      "id": "huntsmans_copse",
      "name": "Huntsman's Copse",
      "description": "Floresta repleta de caçadores e mortos-vivos.",
      "connections": ["undead_purgatory", "harvest_valley", "majula"],
      "required_items": {}
    },
    {
      "id": "undead_purgatory",
      "name": "Undead Purgatory",
      "description": "Área opcional com o chefe Executioner's Chariot.",
      "connections": ["huntsmans_copse"],
      "required_items": {}
    },
    {
      "id": "harvest_valley",
      "name": "Harvest Valley",
      "description": "Área venenosa, caminho até Earthen Peak.",
      "connections": ["earthen_peak", "huntsmans_copse"],
      "required_items": {}
    },
    {
      "id": "earthen_peak",
      "name": "Earthen Peak",
      "description": "Fortaleza cheia de veneno, lar de Mytha.",
      "connections": ["iron_keep", "harvest_valley"],
      "required_items": {}
    },
    {
      "id": "iron_keep",
      "name": "Iron Keep",
      "description": "Fortaleza ardente, lar do Old Iron King.",
      "connections": ["belfry_sol", "majula"],
      "required_items": {}
    },
    {
      "id": "belfry_sol",
      "name": "Belfry Sol",
      "description": "Área opcional acima da Iron Keep.",
      "connections": ["iron_keep"],
      "required_items": {}
    },
    {
      "id": "shaded_woods",
      "name": "Shaded Woods",
      "description": "Floresta enevoada cheia de inimigos invisíveis.",
      "connections": ["doors_of_pharros", "aldias_keep", "majula"],
      "required_items": {
        "aldias_keep": "Emblema do Rei"
      }
    },
    {
      "id": "doors_of_pharros",
      "name": "Doors of Pharros",
      "description": "Ruínas inundadas, lar de ratos e armadilhas.",
      "connections": ["brightstone_cove_tseldora", "shaded_woods"],
      "required_items": {}
    },
    {
      "id": "brightstone_cove_tseldora",
      "name": "Brightstone Cove Tseldora",
      "description": "Caverna infestada por aracnídeos e Prowling Magus.",
      "connections": ["doors_of_pharros"],
      "required_items": {}
    },
    {
      "id": "grave_of_saints",
      "name": "Grave of Saints",
      "description": "Área opcional cheia de ratos e túneis.",
      "connections": ["the_gutter"],
      "required_items": {}
    },
    {
      "id": "the_gutter",
      "name": "The Gutter",
      "description": "Aldeia decadente que leva ao Black Gulch.",
      "connections": ["grave_of_saints", "black_gulch"],
      "required_items": {}
    },
    {
      "id": "black_gulch",
      "name": "Black Gulch",
      "description": "Área infestada de estátuas tóxicas e o Rotten.",
      "connections": ["the_gutter"],
      "required_items": {}
    },
    {
      "id": "drangleic_castle",
      "name": "Drangleic Castle",
      "description": "Castelo central do reino, lar de vários bosses.",
      "connections": ["shrine_of_amana", "shaded_woods"],
      "required_items": {
        "shrine_of_amana": "Emblema do Rei"
      }
    },
    {
      "id": "shrine_of_amana",
      "name": "Shrine of Amana",
      "description": "Santuário submerso, guardado por feiticeiras.",
      "connections": ["undead_crypt", "drangleic_castle"],
      "required_items": {}
    },
    {
      "id": "undead_crypt",
      "name": "Undead Crypt",
      "description": "Mausoléu sombrio, onde reside Velstadt.",
      "connections": ["aldias_keep", "shrine_of_amana"],
      "required_items": {}
    },
    {
      "id": "aldias_keep",
      "name": "Aldia's Keep",
      "description": "Mansão de experimentos grotescos.",
      "connections": ["dragon_aerie", "undead_crypt"],
      "required_items": {}
    },
    {
      "id": "dragon_aerie",
      "name": "Dragon Aerie",
      "description": "Ninho de dragões guardando o caminho final.",
      "connections": ["dragon_shrine", "aldias_keep"],
      "required_items": {}
    },
    {
      "id": "dragon_shrine",
      "name": "Dragon Shrine",
      "description": "Templo guardado por dragões e cavaleiros dracônicos.",
      "connections": [],
      "required_items": {}
    },
    {
      "id": "memory_of_jeigh",
      "name": "Memory of Jeigh",
      "description": "Memória de um Gigante, necessário para avançar ao final.",
      "connections": ["fofg"],
      "required_items": {
        "access": "Ashen Mist Heart"
      }
    },
    {
      "id": "the_pit",
      "name": "The Pit",
      "description": "Buraco profundo em Majula que leva ao Grave of Saints.",
      "connections": ["grave_of_saints", "majula"],
      "required_items": {
        "access": "Anel da Gata ou Feather Fall"
      }
    }
  ]
}

@app.get("/")
async def root():
    return {"Hello World!"}

@app.get("/darksouls2")
async def root():
    return darksouls2

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}