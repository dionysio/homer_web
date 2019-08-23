<template>
  <div>
    <b-form @submit.prevent="sub">
      <b-form-group id="input-group-1">
        <b-form-textarea autofocus="" id="textarea" v-model="text" placeholder="Enter your text..." rows="10" min-rows="3" required v-debounce:500ms="sub" maxlength="100000"></b-form-textarea>
      </b-form-group>
    </b-form>

    <div id="report">
      <transition name="fade">
        <div v-show="showReport">
          <b-row class="text-center">
            <b-col>
              <h1>Report</h1>
              </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-table fixed responsive hover :items="items" id="summary-table" thead-class="hidden_header"></b-table>
            </b-col>
            <b-col cols="6">
              <Paragraph :paragraph=paragraph :labels=labels v-for="paragraph in paragraphs" v-bind:key="paragraph.number"></Paragraph>
            </b-col>
          </b-row>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import $backend from '../backend'
import Paragraph from '../components/Paragraph'

export default {
  name: 'TextAnalysis',
  components: {
    Paragraph
  },
  data () {
    return {
      showReport: false,
      text: '',
      summary: {},
      paragraphs: [],
      labels: {
        'reading_time': 'Reading time',
        'flesch_reading': 'Flesch reading score',
        'dale_chall': 'Dale Chall reading score',
        'total_words': 'Total words',
        'and_frequency': '"and" frequency',

        'total_sentences': 'Total sentences',
        'avg_words_per_sentence': 'Average words per sentence',
        'longest_sentence': 'Longest sentence',
        'len_of_longest_sentence': 'Length of longest sentence',

        'total_paragraphs': 'Total paragraphs',
        'avg_sentences_per_para': 'Average sentences per paragraph',
        'len_of_longest_paragraph': 'Length of longest paragraph',

        'compulsive_hedgers': 'Compulsive hedgers',
        'intensifiers': 'Intensifiers',
        'vague_words': 'Vague words'
      }
    }
  },
  methods: {
    sub: function (event) {
      if (this.text) {
        this.showReport = true
        this.$scrollTo('#report', 500, { easing: 'ease-in' })
        $backend.fetchStats(this.text)
          .then(data => {
            this.summary = data.summary
            this.paragraphs = data.paragraphs
            this.$root.$emit('bv::refresh::table', 'summary-table')
          })
      }
      return true
    },
    items: function (ctx) {
      let items = []
      for (const [key, value] of Object.entries(this.labels)) {
        items.push({ 'label': value, 'value': this.summary[key] || '' })
      }
      return items
    }
  }
}
</script>

<style>
.hidden_header {
  display: none;
}

table td:first-child  {
  text-align: right;
  border-right: 1px solid black;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

</style>
