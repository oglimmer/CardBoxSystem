<script setup>
import { ref } from 'vue'
import axios from 'axios'
const items = ref([])

async function init() {
  const { data } = await axios.get("http://localhost:8000/cards")
  items.value = data
}
void init();

async function removeItem(id) {
  await axios.delete("http://localhost:8000/cards/" + id)
  items.value = items.value.filter(e => e.id !== id)
}

const word = ref("")
const description = ref("")

async function save() {
  const { data } = await axios.post("http://localhost:8000/cards", {
    word: word.value,
    description: description.value
  })
  items.value.push(data)
  word.value = ""
  description.value = ""
}

const no = ref("")
const wordToShow = ref("")
const descriptionToShow = ref("")
const wordVisibility = ref("hidden")
const descriptionVisibility = ref("hidden")

async function ask(e) {
  e.preventDefault()
  const item = items.value.filter(e => e.id == no.value)[0]
  wordToShow.value = item.word
  descriptionToShow.value = item.description
  wordVisibility.value = ""
}

function next() {
  descriptionVisibility.value = ""
}

function done() {
  wordVisibility.value = "hidden"
  descriptionVisibility.value = "hidden"
}

</script>

<template>
  <h3>Liste</h3>
  <li v-for="item in items">
    #{{ item.id }}  - {{ item.word }} - <span @click="removeItem(item.id)">[del]</span>
  </li>

  <h3>Adding an item</h3>
  <form @submit.prevent="save">
    Word: <input name="word" v-model="word" /> <br />
    Description: <textarea name="description" v-model="description"></textarea> <br />
    <button>Save</button>
  </form>

  <h3>Tester</h3>
  <form>
    #: <input name="no" v-model="no" /> <button @click="ask">Ask</button>
    <div :style="{'visibility':wordVisibility}">
      Word: {{ wordToShow }} <span @click="next">[next]</span>
    </div>
    <div :style="{'visibility':descriptionVisibility}">
      Description: {{ descriptionToShow }} <span @click="done">[done]</span>
    </div>
  </form>

</template>

<style scoped>

</style>
