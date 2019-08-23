<template>
  <footer>
    <nav class="footer navbar fixed-bottom">
      <p class="font-weight-light">
        Props to <a href="https://github.com/wyounas/homer">Waqas Younas</a> for his original project
      </p>
    </nav>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>
.footer {
  justify-content: flex-end !important;
  padding-bottom: 0 !important;
  background: white;
}
.footer > p {
  margin: 0
}
</style>
