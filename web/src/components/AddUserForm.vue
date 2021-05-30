<template>
  <v-row>
    <v-col cols="12" class="pa-6 pa-lg-12">
      <v-card elevation="2" class="px-lg-12 primaryFont">
        <v-card-title>Add new contact</v-card-title>
        <v-card-text>
          <v-form ref="userForm" v-model="valid" lazy-validation>
            <v-row>
              <v-col cols="12" lg="6">
                <v-text-field
                  v-model="firstName"
                  :counter="20"
                  :rules="nameRules"
                  label="First Name"
                  required
                />
              </v-col>
              <v-col cols="12" lg="6">
                <v-text-field
                  v-model="lastName"
                  :counter="20"
                  :rules="nameRules"
                  label="Last Name"
                  required
                />
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" lg="6">
                <v-text-field
                  v-model="emailAddress"
                  :rules="emailRules"
                  label="E-mail"
                  required
                />
              </v-col>
              <v-col cols="12" lg="6">
                <v-text-field
                  v-model="mobileNumber"
                  :rules="mobileRules"
                  label="Mobile Number"
                  required
                />
              </v-col>
            </v-row>

            <v-btn
              :disabled="!valid"
              color="secondary"
              class="mr-4"
              :loading="isPosting"
              @click="submit"
            >
              <v-icon left dark> mdi-check </v-icon>
              Save
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";

export default {
  data: () => ({
    valid: true,
    firstName: "",
    lastName: "",
    emailAddress: "",
    mobileNumber: "",
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
  }),
  computed: {
    ...mapState(["isPosting"]),
  },
  methods: {
    submit() {
      if (this.$refs.userForm.validate()) {
        const formData = {
          emailAddress: this.emailAddress,
          firstName: this.firstName,
          lastName: this.lastName,
          mobileNumber: this.mobileNumber,
        };

        this.$store.dispatch("addUser", formData).then(() => {
          this.$refs.userForm.reset();
        });
      }
    },
  },
};
</script>
