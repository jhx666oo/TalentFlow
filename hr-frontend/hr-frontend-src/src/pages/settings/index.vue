<template>
  <div class="max-w-2xl mx-auto">
    <h1 class="text-2xl font-bold text-gray-900 mb-8">设置</h1>

    <!-- 钉钉绑定 -->
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-lg font-semibold text-gray-900">钉钉账号绑定</h2>
          <p class="text-sm text-gray-500 mt-1">
            绑定钉钉后，AI 可自动查询面试官空闲时间并在钉钉创建面试日程
          </p>
        </div>
        <div>
          <template v-if="dingtalkLoading">
            <el-button loading disabled>加载中</el-button>
          </template>
          <template v-else-if="dingtalkUser">
            <el-tag type="success" size="large" effect="plain">
              {{ dingtalkUser.nick }}
            </el-tag>
          </template>
          <template v-else>
            <el-button type="primary" @click="bindDingtalk">
              <el-icon class="mr-1"><Link /></el-icon>
              绑定钉钉
            </el-button>
          </template>
        </div>
      </div>
      <div v-if="dingtalkUser" class="mt-3 text-sm text-gray-400">
        已绑定手机号：{{ dingtalkUser.mobile || '未知' }}
      </div>
    </div>

    <!-- 系统信息 -->
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-lg font-semibold text-gray-900 mb-4">系统信息</h2>
      <el-descriptions :column="1" border size="small">
        <el-descriptions-item label="系统名称">TalentFlow 智能招聘系统</el-descriptions-item>
        <el-descriptions-item label="版本">v1.0.0</el-descriptions-item>
        <el-descriptions-item label="API 地址">https://api.ai-bot.icu</el-descriptions-item>
      </el-descriptions>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { Link } from '@element-plus/icons-vue'
import { getDingtalkAuthorizeUrl, getDingtalkStatus } from '@/apis/user_api'

interface DingtalkInfo {
  nick: string
  mobile: string
  union_id: string
  open_id: string
}

const dingtalkLoading = ref(true)
const dingtalkUser = ref<DingtalkInfo | null>(null)

const fetchDingtalkStatus = async () => {
  dingtalkLoading.value = true
  try {
    const data = await getDingtalkStatus()
    dingtalkUser.value = data.dingding_user
  } catch {
    dingtalkUser.value = null
  } finally {
    dingtalkLoading.value = false
  }
}

const bindDingtalk = async () => {
  try {
    const data = await getDingtalkAuthorizeUrl()
    // 跳转到钉钉授权页面
    window.location.href = data.authorize_url
  } catch {
    ElMessage.error('获取钉钉授权链接失败')
  }
}

onMounted(() => {
  fetchDingtalkStatus()
})
</script>
