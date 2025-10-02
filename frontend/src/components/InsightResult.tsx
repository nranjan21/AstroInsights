'use client';

import { motion } from 'framer-motion';
import { Sparkles, Star } from 'lucide-react';
import { InsightResponse } from '@/types';
import { ZODIAC_DATA } from '@/lib/zodiac';

interface InsightResultProps {
  result: InsightResponse;
}

export default function InsightResult({ result }: InsightResultProps) {
  const zodiacInfo = ZODIAC_DATA[result.zodiac] || {
    name: result.zodiac,
    symbol: '✨',
    element: 'Unknown',
    dates: '',
    traits: [],
    colors: ['#6366F1']
  };

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
      className="card p-8"
    >
      {/* Zodiac Header */}
      <div className="text-center mb-6">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
          className="text-6xl mb-4"
        >
          {zodiacInfo.symbol}
        </motion.div>
        <h2 className="text-3xl font-bold text-gray-800 mb-2">{zodiacInfo.name}</h2>
        <div className="flex items-center justify-center space-x-4 text-sm text-gray-600">
          <span className="px-3 py-1 bg-gray-100 rounded-full">{zodiacInfo.element}</span>
          <span>{zodiacInfo.dates}</span>
        </div>
      </div>

      {/* Insight Card */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="bg-gradient-to-br from-primary-50 to-cosmic-50 border border-primary-200 rounded-2xl p-6 mb-6"
      >
        <div className="flex items-start space-x-3">
          <Sparkles className="w-6 h-6 text-primary-500 mt-1 flex-shrink-0" />
          <div>
            <h3 className="font-semibold text-gray-800 mb-2">Your Daily Insight</h3>
            <p className="text-gray-700 leading-relaxed text-lg">
              {result.insight}
            </p>
          </div>
        </div>
      </motion.div>

      {/* Zodiac Traits */}
      {zodiacInfo.traits.length > 0 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6 }}
          className="mb-6"
        >
          <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
            <Star className="w-5 h-5 mr-2 text-yellow-500" />
            Key Traits
          </h4>
          <div className="flex flex-wrap gap-2">
            {zodiacInfo.traits.map((trait, index) => (
              <motion.span
                key={trait}
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.8 + index * 0.1 }}
                className="px-3 py-1 bg-gradient-to-r from-primary-100 to-cosmic-100 text-primary-700 rounded-full text-sm font-medium"
              >
                {trait}
              </motion.span>
            ))}
          </div>
        </motion.div>
      )}


      {/* Language Badge */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1 }}
        className="mt-4 text-center"
      >
        <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600">
          Language: {result.language.toUpperCase()}
        </span>
      </motion.div>
    </motion.div>
  );
}
