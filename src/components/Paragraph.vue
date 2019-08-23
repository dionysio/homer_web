<template>
 <b-table fixed hover responsive :items="items" :fields="fields"></b-table>
</template>

<script>
export default {
  name: 'Paragraph',
  props: {
    labels: {},
    paragraph: {}
  },
  data () {
    return {
      fields: {
        'label': {'label': 'Paragraph #' + this.paragraph.number},
        'value': {'label': ''}
      }
    }
  },
  methods: {
    items: function (ctx) {
      let items = []

      for (const [key, value] of Object.entries(this.paragraph)) {
        if (this.labels[key]) {
          items.push({'label': this.labels[key], 'value': value})
        }
      }

      return items
    }
  }
}
</script>
