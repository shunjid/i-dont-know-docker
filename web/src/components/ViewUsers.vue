<template>
  <div>
    <v-row>
      <v-col cols="12" class="primaryFont">
        <h2 class="text-center primary--text">Contact List</h2>
        <p class="mt-4 text-center">
          Fields with <b class="secondary--text">[*]</b> marked headers are
          editable. Click on following data cells in the table to edit.
        </p>
      </v-col>
    </v-row>
    <v-skeleton-loader type="table" :loading="isFetching" v-if="isFetching" />
    <v-row>
      <v-col cols="12" class="pa-lg-12">
        <v-data-table
          :headers="headers"
          :items="users"
          :items-per-page="5"
          class="elevation-0 primaryFont"
        >
          <template v-slot:[`item.firstName`]="props">
            <v-edit-dialog
              :return-value.sync="props.item.firstName"
              @save="save(props.item)"
              large
              persistent
            >
              {{ props.item.firstName }}
              <template v-slot:input>
                <v-text-field
                  v-model="props.item.firstName"
                  :rules="nameRules"
                  label="Edit"
                  single-line
                  counter="20"
                  autocomplete="off"
                />
              </template>
            </v-edit-dialog>
          </template>

          <template v-slot:[`item.lastName`]="props">
            <v-edit-dialog
              :return-value.sync="props.item.lastName"
              @save="save(props.item)"
              large
              persistent
            >
              {{ props.item.lastName }}
              <template v-slot:input>
                <v-text-field
                  v-model="props.item.lastName"
                  :rules="nameRules"
                  label="Edit"
                  single-line
                  counter="20"
                  autocomplete="off"
                />
              </template>
            </v-edit-dialog>
          </template>

          <template v-slot:[`item.mobile`]="props">
            <v-edit-dialog
              :return-value.sync="props.item.mobile"
              @save="save(props.item)"
              large
              persistent
            >
              {{ props.item.mobile }}
              <template v-slot:input>
                <v-text-field
                  v-model="props.item.mobile"
                  :rules="mobileRules"
                  label="Edit"
                  single-line
                  autocomplete="off"
                />
              </template>
            </v-edit-dialog>
          </template>

          <template v-slot:[`item.email`]="props">
            <v-edit-dialog
              :return-value.sync="props.item.email"
              @save="save(props.item)"
              large
              persistent
            >
              {{ props.item.email }}
              <template v-slot:input>
                <v-text-field
                  v-model="props.item.email"
                  :rules="emailRules"
                  label="Edit"
                  single-line
                  autocomplete="off"
                />
              </template>
            </v-edit-dialog>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon class="error--text" small @click="deleteItem(item)">
              mdi-delete
            </v-icon>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card class="primaryFont">
        <v-card-title>
          Are you sure you want to delete this contact?
        </v-card-title>
        <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm">
            OK
          </v-btn>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-dialog>
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
        { text: "First Name (*)", value: "firstName" },
        { text: "Last Name  (*)", value: "lastName" },
        { text: "Mobile  (*)", value: "mobile" },
        { text: "Email  (*)", value: "email" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      dialogDelete: false,
      deletionDesiredId: -1,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
      mobileRules: [
        (v) => !!v || "Mobile is required",
        (v) =>
          /^(?:\+?88)?01[13-9]\d{8}$/.test(v) ||
          "Invalid Bangladeshi Mobile Number",
      ],
    };
  },
  computed: {
    ...mapState(["users", "isFetching"]),
  },
  created() {
    this.$store.dispatch("getUsers");
  },
  methods: {
    save(contact) {
      this.$store.dispatch("updateUser", contact);
    },
    deleteItem(item) {
      this.dialogDelete = true;
      this.deletionDesiredId = item.id;
    },
    closeDelete() {
      this.dialogDelete = false;
      this.deletionDesiredId = -1;
    },
    deleteItemConfirm() {
      this.$store
        .dispatch("deleteUser", this.deletionDesiredId)
        .then(() => this.closeDelete());
    },
  },
};
</script>

<style lang="scss" scoped></style>
