<template>
  <div class="flex min-h-screen">
    <!-- Left: Brand Panel -->
    <div class="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 relative overflow-hidden">
      <!-- Decorative blobs -->
      <div class="absolute -top-40 -left-40 w-80 h-80 bg-indigo-500/20 rounded-full blur-3xl" />
      <div class="absolute top-1/2 -right-20 w-72 h-72 bg-blue-500/15 rounded-full blur-3xl" />
      <div class="absolute -bottom-32 left-1/3 w-64 h-64 bg-violet-500/15 rounded-full blur-3xl" />

      <!-- Grid pattern overlay -->
      <div
        class="absolute inset-0 opacity-[0.03]"
        style="background-image: radial-gradient(circle, rgb(255 255 255) 1px, transparent 1px); background-size: 32px 32px;"
      />

      <div class="relative flex flex-col justify-center px-16 w-full max-w-xl mx-auto">
        <!-- Logo -->
        <div class="flex items-center gap-3 mb-8">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-400 to-blue-500 flex items-center justify-center shadow-lg shadow-indigo-500/25">
            <svg class="w-7 h-7 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" />
            </svg>
          </div>
          <span class="text-2xl font-bold text-white tracking-tight">TalentFlow</span>
        </div>

        <h1 class="text-3xl font-bold text-white leading-tight mb-4">
          {{ title }}
        </h1>
        <p class="text-lg text-indigo-200/80 leading-relaxed">
          {{ subtitle }}
        </p>

        <!-- Feature highlights -->
        <div class="mt-12 space-y-5">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 rounded-lg bg-indigo-500/20 flex items-center justify-center flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4 text-indigo-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-white">AI 简历解析</p>
              <p class="text-sm text-indigo-300/60">智能提取候选人信息，告别手动录入</p>
            </div>
          </div>
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 rounded-lg bg-blue-500/20 flex items-center justify-center flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4 text-blue-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5" />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-white">全流程管理</p>
              <p class="text-sm text-indigo-300/60">从简历筛选到面试入职，一站式管理</p>
            </div>
          </div>
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 rounded-lg bg-violet-500/20 flex items-center justify-center flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4 text-violet-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5M9 7.5h6M9 11.25h3" />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-white">多角色协同</p>
              <p class="text-sm text-indigo-300/60">HR、面试官、管理员高效协同工作</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Right: Form Panel -->
    <div class="flex flex-1 flex-col justify-center px-6 py-12 bg-white sm:px-12 lg:px-16">
      <div class="w-full max-w-md mx-auto">
        <!-- Mobile logo (visible only on small screens) -->
        <div class="lg:hidden text-center mb-10">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-blue-600 flex items-center justify-center mx-auto shadow-lg shadow-indigo-500/25">
            <svg class="w-7 h-7 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" />
            </svg>
          </div>
          <h2 class="mt-4 text-xl font-bold text-gray-900">{{ title }}</h2>
        </div>

        <div class="lg:hidden">
          <p v-if="subtitle" class="text-center text-sm text-gray-500 mb-8">{{ subtitle }}</p>
        </div>

        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string
  subtitle?: string
}

defineProps<Props>()
</script>
