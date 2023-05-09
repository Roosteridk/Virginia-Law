import { defineConfig } from 'vitepress'
import sb from '../sidebar.json'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Virginia Law",
  description: "A VitePress Site",
  ignoreDeadLinks: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Virginia Code', link: '/vacode'},
      { text: 'Examples', link: '/markdown-examples' }
    ],
    sidebar: {
      '/vacode': sb
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
