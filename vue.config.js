module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api*': {
        target: 'https://goodwriter.dionysio.com/'
      }
    }
  }
}
