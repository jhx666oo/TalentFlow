<template>
  <AuthLayout title="TalentFlow 智能招聘系统" subtitle="AI 驱动的全流程智能招聘管理平台">
    <div class="mb-8">
      <h2 class="text-2xl font-bold text-gray-900">欢迎回来</h2>
      <p class="mt-1 text-sm text-gray-500">登录您的账户以继续</p>
    </div>

    <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      :rules="rules"
      label-position="top"
      class="space-y-5"
      @submit.prevent="submitForm(ruleFormRef)"
    >
      <el-form-item label="邮箱地址" prop="email">
        <el-input
          v-model="ruleForm.email"
          size="large"
          placeholder="请输入邮箱地址"
          :prefix-icon="Message"
        />
      </el-form-item>

      <el-form-item label="密码" prop="password">
        <el-input
          v-model="ruleForm.password"
          type="password"
          size="large"
          placeholder="请输入密码"
          show-password
          :prefix-icon="Lock"
        />
      </el-form-item>

      <div class="flex items-center justify-between text-sm">
        <label class="flex items-center gap-1.5 text-gray-500 cursor-pointer">
          <input type="checkbox" class="rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
          记住我
        </label>
      </div>

      <el-button type="primary" native-type="submit" class="w-full !h-11 !text-base !font-medium !rounded-lg" size="large">
        登录
      </el-button>
    </el-form>

    <p class="mt-8 text-center text-sm text-gray-500">
      还没有账户？
      <router-link to="/register" class="font-semibold text-indigo-600 hover:text-indigo-500">
        立即注册
      </router-link>
    </p>
  </AuthLayout>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import AuthLayout from '@/components/AuthLayout.vue'
import { login, type LoginData } from '@/apis/user_api'
import { useUserStore } from '@/stores/user'
import { Message, Lock } from '@element-plus/icons-vue'

const router = useRouter()
const ruleFormRef = ref<FormInstance>()

const ruleForm = reactive({
  email: '',
  password: '',
})

const rules = reactive<FormRules<typeof ruleForm>>({
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] },
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 20, message: '密码长度应为 6 到 20 个字符', trigger: 'blur' },
  ],
})

async function submitForm(formEl: FormInstance | undefined) {
  if (!formEl) return
  await formEl.validate(async (valid) => {
    if (valid) {
      try {
        const res = await login(ruleForm as LoginData)
        const user = res.user
        const accessToken = res.access_token
        const userStore = useUserStore()
        userStore.login(user, accessToken)
        ElMessage.success('登录成功')
        router.push('/')
      } catch (error) {
        ElMessage.error('登录失败，请检查您的邮箱和密码！')
      }
    } else {
      ElMessage.error('请修正表单中的错误')
    }
  })
}
</script>
