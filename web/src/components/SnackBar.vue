<template>
  <v-snackbar v-model="show" :color="color" bottom center>
    {{ text }}
    <template v-slot:action="{ attrs }">
      <v-btn color="white" light v-bind="attrs" @click="show = false">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  data: () => ({
    show: false,
    color: "",
    text: "",
  }),
  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === "SHOW_SNACKBAR") {
        this.text = state.snackbarText;
        this.color = state.snackbarColor;
        this.show = true;
      }
    });
  },
};
</script>
