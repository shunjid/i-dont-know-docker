<template>
  <div>
    <add-user-form />
    <view-users />
  </div>
</template>

<script>
import AddUserForm from "../components/AddUserForm.vue";
import ViewUsers from "../components/ViewUsers.vue";
export default {
  components: { AddUserForm, ViewUsers },
};
</script>

<style lang="scss" scoped></style>
