import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
  root: '.',
  server: {
    host: '0.0.0.0',
    port: 5000,
  },
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: ['index.html', 'exam.html'],
    },
  },
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'cases',
          dest: '.',
        },
        {
          src: 'sw.js',
          dest: '.',
        },
        {
          src: 'manifest.json',
          dest: '.',
        },
        {
          src: 'icons',
          dest: '.',
        },
      ],
    }),
  ],
});
