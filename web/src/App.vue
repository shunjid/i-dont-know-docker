<template>
  <v-app>
    <app-bar />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "./components/AppBar.vue";
export default {
  components: { AppBar },
  name: "App",

  data: () => ({
    //
  }),
};
</script>

<style>
.primaryFont {
  font-family: "Google Sans", Courier, monospace;
}
</style>
