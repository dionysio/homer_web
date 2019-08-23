<template>
  <div>
    <Header />
    <b-container>
      <TextAnalysis />
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import TextAnalysis from '../components/TextAnalysis'
import Footer from '../components/Footer'

export default {
  name: 'Home',
  components: {
    Header,
    TextAnalysis,
    Footer
  }
}
</script>
