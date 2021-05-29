<template>
  <div>
    <add-user-form />
    <view-users />
    <snack-bar />
  </div>
</template>

<script>
import AddUserForm from "../components/AddUserForm.vue";
import SnackBar from "../components/SnackBar.vue";
import ViewUsers from "../components/ViewUsers.vue";
export default {
  components: { AddUserForm, ViewUsers, SnackBar },
};
</script>

<style lang="scss" scoped></style>
