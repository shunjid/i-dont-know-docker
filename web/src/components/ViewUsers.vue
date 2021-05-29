<template>
  <div>
    <v-row>
      <v-col cols="12" class="primaryFont">
        <h2 class="text-center">Contact List</h2>
      </v-col>
    </v-row>
    <v-skeleton-loader type="table" :loading="isFetching" v-if="isFetching" />
    <v-row>
      <v-col cols="12" class="pa-12">
        <v-data-table
          :headers="headers"
          :items="users"
          :items-per-page="5"
          class="elevation-0"
        ></v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      headers: [
        {
          text: "Id",
          align: "start",
          value: "id",
        },
        { text: "First Name", value: "firstName" },
        { text: "Last Name", value: "lastName" },
        { text: "Mobile", value: "mobile" },
        { text: "Email", value: "email" },
      ],
    };
  },
  computed: {
    ...mapState(["users", "isFetching"]),
  },
  created() {
    this.$store.dispatch("getUsers");
  },
};
</script>

<style lang="scss" scoped></style>
