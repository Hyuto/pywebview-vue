<template>
  <div class="hello">
    <h2>{{ msg }}</h2>
    <p>
      Hello <code>{{ username }}!</code> Please Edit <code>src/App.vue</code>
      save and refresh to apply changes.
    </p>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "Hello",
  props: {
    msg: String,
  },
  setup() {
    const username = ref("");

    // getusername
    window.addEventListener("pywebviewready", () => {
      window.pywebview.api.GetUsername().then((response) => {
        username.value = response.user;
      });
    });

    return {
      username,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
p {
  line-height: 1.5rem;

  code {
    font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New", monospace;
    color: #b6c33c;
    background-color: #2c3e50;
    padding: 5px;
    border-radius: 5px;
  }
}
</style>
