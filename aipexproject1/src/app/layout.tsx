import type { Metadata } from 'next'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Medical Assistant',
  description: 'I am a virtual assistant',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
        {/* Include any additional meta tags or links to stylesheets/fonts here */}
        <style>{`
          body {
            background: linear-gradient(to bottom,#6dd5ed,#fff);
            min-height: 100vh;
            position: relative;
          }
          header {
            text-align: center;
            color: #fff;
            margin-bottom: 70px;
            font-size: 3rem; /* Adjust the font size as needed */
            font-weight: bold; 
          }
        `}</style>
      </head>
      <body className={`flex flex-col items-center ${inter.className ?? ''}`}>
        <header>
          <h1>Medical Assistant</h1>
        </header>
        <div className="flex justify-center items-center flex-1">
          {children}
        </div>
        <div style={{ position: 'absolute', top: 20, right: 20, textAlign: 'center', color: '#fff' }}>
        </div>
      </body>
    </html>
  )
}
