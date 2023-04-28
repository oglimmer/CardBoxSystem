from typing import List
from fastapi import FastAPI, Response, status
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os.path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DATABASE_FILE= "LibaryAndStorage/words.json"

class Card(BaseModel):
    id: int | None = None
    word: str
    description: str

class CardList(BaseModel):
    __root__: List[Card]

def read_from_disk():
  cards = CardList(__root__=[])
  if os.path.isfile(DATABASE_FILE):
    with open(DATABASE_FILE, "r") as f:
        cards_json = json.load(f)
    for card_json in cards_json:
        card = Card.parse_obj(card_json)
        cards.__root__.append(card)
  return cards

def get_max_id(cards: CardList):
    maxId = 0
    for card in cards.__root__:
        if maxId < card.id:
            maxId = card.id
    return maxId

@app.get("/cards")
async def read_all():
    return read_from_disk()

@app.get("/cards/{card_id}")
async def read_card(card_id: int):
    cards = read_from_disk()
    for card in cards.__root__:
        if card_id == card.id:
            return card
    return Response(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/cards", status_code=201)
async def create_card(card: Card):
    print("foo")
    cards = read_from_disk()
    newId = get_max_id(cards) + 1
    card.id = newId
    cards.__root__.append(card)
    cards_json = cards.json()
    with open(DATABASE_FILE, "w") as f:
        f.write(cards_json)
    return card


@app.delete("/cards/{card_id}")
async def create_card(card_id: int):
    cards = read_from_disk()
    cardToRemove = None
    for card in cards.__root__:
        if card_id == card.id:
            cardToRemove = card
    if cardToRemove is None:
      return Response(status_code=status.HTTP_404_NOT_FOUND)
    cards.__root__.remove(cardToRemove)    
    cards_json = cards.json()
    with open(DATABASE_FILE, "w") as f:
        f.write(cards_json)
    return Response(status_code=status.HTTP_200_OK)
