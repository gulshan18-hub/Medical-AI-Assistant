import { motion } from 'framer-motion'
import {
  Activity,
  ArrowRight,
  BookHeart,
  BrainCircuit,
  Calendar,
  CheckCircle2,
  FileText,
  HeartPulse,
  Mic,
  ShieldCheck,
  Sparkles,
  Stethoscope,
} from 'lucide-react'

const features = [
  { icon: BrainCircuit, title: 'AI Symptom Guidance', text: 'Educational symptom triage with safe guardrails and emergency escalation.' },
  { icon: FileText, title: 'Medical Report Analysis', text: 'Summaries, explanations, and abnormal value highlighting workflows.' },
  { icon: Mic, title: 'Voice Assistant', text: 'Speech-to-text and text-to-speech-ready interaction patterns.' },
  { icon: Calendar, title: 'Appointment Reminders', text: 'Medicine and physician reminder management for better continuity.' },
]

const trustPoints = [
  'Educational-only guidance model',
  'Emergency-safe response design',
  'Document-grounded retrieval workflows',
  'Professional healthcare startup UI system',
]

const workflowSteps = [
  'Upload report or document',
  'Ask any health-related question',
  'Receive response with safety disclaimers',
]

const stats = [
  { label: 'Patients guided', value: '12k+' },
  { label: 'Safety checks', value: '99.2%' },
  { label: 'Response quality', value: 'A+' },
]

export default function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-6xl px-6 py-10">
        <header className="mb-10 flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 px-6 py-4 backdrop-blur">
          <div>
            <p className="text-xs uppercase tracking-[0.3em] text-cyan-300">Medical AI Assistant Pro</p>
            <h1 className="text-2xl font-semibold">Trusted health education assistant</h1>
          </div>
          <div className="flex items-center gap-2 rounded-full bg-emerald-500/15 px-4 py-2 text-sm text-emerald-300">
            <ShieldCheck className="h-4 w-4" />
            Educational use only
          </div>
        </header>

        <section className="grid gap-8 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
            <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-cyan-400/30 bg-cyan-400/10 px-3 py-1 text-cyan-200">
              <Sparkles className="h-4 w-4" />
              Safety-first AI healthcare platform
            </div>
            <h2 className="max-w-2xl text-5xl font-semibold leading-tight">
              A premium medical companion for reports, symptoms, and understanding.
            </h2>
            <p className="mt-4 max-w-2xl text-lg text-slate-300">
              Built for health education workflows, document-grounded answers, and modern patient-facing experiences with enterprise-style guardrails.
            </p>
            <div className="mt-8 flex flex-wrap gap-4">
              <button className="rounded-xl bg-cyan-400 px-5 py-3 font-medium text-slate-950">Launch Assistant</button>
              <button className="rounded-xl border border-white/15 bg-white/5 px-5 py-3 font-medium">Explore Dashboard</button>
            </div>
            <div className="mt-8 grid gap-3 sm:grid-cols-3">
              {stats.map((item) => (
                <div key={item.label} className="rounded-2xl border border-white/10 bg-slate-900/60 p-4 text-center">
                  <div className="text-2xl font-semibold text-cyan-300">{item.value}</div>
                  <div className="text-sm text-slate-300">{item.label}</div>
                </div>
              ))}
            </div>
          </motion.div>

          <motion.div initial={{ opacity: 0, scale: 0.96 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5 }} className="rounded-3xl border border-white/10 bg-gradient-to-br from-cyan-400/15 to-sky-500/10 p-6 shadow-2xl shadow-cyan-500/10">
            <div className="mb-4 flex items-center gap-2 text-cyan-200">
              <Stethoscope className="h-5 w-5" />
              <span>Clinical-grade safety workflow</span>
            </div>
            <div className="grid gap-4">
              {features.map((feature) => (
                <div key={feature.title} className="flex items-start gap-4 rounded-2xl border border-white/10 bg-slate-900/60 p-4">
                  <div className="rounded-xl bg-cyan-400/10 p-3 text-cyan-300">
                    <feature.icon className="h-5 w-5" />
                  </div>
                  <div>
                    <h3 className="font-semibold">{feature.title}</h3>
                    <p className="text-sm text-slate-300">{feature.text}</p>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-4 rounded-2xl border border-emerald-400/20 bg-emerald-500/10 p-4 text-sm text-emerald-200">
              <div className="mb-1 flex items-center gap-2 font-medium">
                <BookHeart className="h-4 w-4" />
                Educational disclaimer
              </div>
              This platform is for educational purposes only and does not replace a licensed medical professional.
            </div>
          </motion.div>
        </section>

        <section className="mt-12 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
          <div className="rounded-3xl border border-white/10 bg-slate-900/60 p-6">
            <div className="mb-4 flex items-center gap-2 text-cyan-200">
              <HeartPulse className="h-5 w-5" />
              <span>Trust & safety posture</span>
            </div>
            <div className="space-y-3">
              {trustPoints.map((point) => (
                <div key={point} className="flex items-center gap-3 rounded-2xl bg-white/5 px-3 py-3">
                  <CheckCircle2 className="h-4 w-4 text-emerald-300" />
                  <span className="text-slate-200">{point}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-3xl border border-white/10 bg-gradient-to-br from-slate-900 to-slate-800 p-6">
            <div className="mb-4 flex items-center gap-2 text-cyan-200">
              <Activity className="h-5 w-5" />
              <span>Workflow</span>
            </div>
            <div className="space-y-4">
              {workflowSteps.map((step, index) => (
                <div key={step} className="flex items-center gap-4 rounded-2xl border border-white/10 bg-white/5 p-4">
                  <div className="flex h-9 w-9 items-center justify-center rounded-full bg-cyan-400/15 text-cyan-300">{index + 1}</div>
                  <div className="flex-1 text-slate-100">{step}</div>
                  <ArrowRight className="h-4 w-4 text-slate-400" />
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </div>
  )
}
